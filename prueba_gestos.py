"""
EV3 + MediaPipe — Control avanzado con 3 MOTORES (USB).

NUEVOS CONTROLES:
- 0 Dedos (Palma cerrada) = Reversa
- 4 Dedos (Palma abierta) = Avanzar
- 3 Dedos = Freno total / Stop
- GESTO SHAKA 🤙 (Pulgar + Meñique) = LEVANTAR (Motor Mediano Adelante)
- GESTO PISTOLA DOBLE (Pulgar + Índice + Medio) = BAJAR (Motor Mediano Atrás)
- 1 Dedo (Índice solo) = Girar Izquierda
- 2 Dedos (Paz) = Girar Derecha
- Seguridad "Jaeger" activa (Quitar la mano frena el robot).
"""

from pathlib import Path
import time

import cv2
import ev3_dc as ev3
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

MODELO = Path(__file__).resolve().parent.parent / "models" / "hand_landmarker.task"
CAMARA = 0

# Definición de todos los puertos
PUERTO_IZQ = ev3.PORT_A
PUERTO_DER = ev3.PORT_C
PUERTO_MEDIANO = ev3.PORT_D # <-- Tu motor mediano

# ---------------------------------------------------------------------------
# decidir_movimiento(lm)
# ---------------------------------------------------------------------------
def decidir_movimiento(lm) -> tuple[str, int]:
    # Detectamos qué dedos específicos están levantados (Verdadero o Falso)
    pulgar = lm[4].y < lm[2].y
    indice = lm[8].y < lm[6].y
    medio = lm[12].y < lm[10].y
    anular = lm[16].y < lm[14].y
    menique = lm[20].y < lm[18].y

    # Contamos cuántos de los 4 dedos principales (sin pulgar) están arriba
    dedos_levantados = sum([indice, medio, anular, menique])

    # 1. LEVANTAR (MOTOR MEDIANO ADELANTE): "Shaka" 🤙 (Pulgar y Meñique arriba)
    if pulgar and menique and not indice and not medio and not anular:
        return ("mediano_adelante", 75)

    # 2. BAJAR (MOTOR MEDIANO ATRÁS): "Pistola Doble" (Pulgar, Índice y Medio arriba)
    if pulgar and indice and medio and not anular and not menique:
        return ("mediano_atras", 75)

    # 3. Gestos basados en cantidad de dedos (VELOCIDADES REDUCIDAS)
    if dedos_levantados == 0:
        return ("reversa", 15)   # Palma cerrada (Puño) -> Reversa (Bajó de 60 a 35)
            
    elif dedos_levantados == 1:
        return ("izquierda", 12) # 1 dedo -> Girar Izquierda (Bajó de 40 a 25)
        
    elif dedos_levantados == 2:
        return ("derecha", 12)   # 2 dedos -> Girar Derecha (Bajó de 40 a 25)
        
    elif dedos_levantados == 3:
        return ("stop", 0)       # 3 dedos -> Frenar / Stop
        
    elif dedos_levantados == 4:
        return ("avanzar", 15)   # Palma abierta (4 dedos) -> Avanzar (Bajó de 60 a 35)

    return ("stop", 0)


def main() -> None:
    if not MODELO.exists():
        raise FileNotFoundError(f"Falta el modelo: {MODELO}")

    # Conectar EV3 y definir los TRES MOTORES
    brick = ev3.EV3(protocol=ev3.USB)
    motor_b = ev3.Motor(PUERTO_IZQ, ev3_obj=brick)
    motor_c = ev3.Motor(PUERTO_DER, ev3_obj=brick)
    motor_mediano = ev3.Motor(PUERTO_MEDIANO, ev3_obj=brick)
    
    estado_actual = ("stop", 0)

    options = vision.HandLandmarkerOptions(
        base_options=mp_python.BaseOptions(model_asset_path=str(MODELO)),
        running_mode=vision.RunningMode.VIDEO,
        num_hands=1,
    )
    landmarker = vision.HandLandmarker.create_from_options(options)

    cap = cv2.VideoCapture(CAMARA)
    if not cap.isOpened():
        brick.__exit__(None, None, None)
        raise RuntimeError("No se pudo abrir la cámara")

    print("EV3 Gestos Listo. Muestra los dedos. Q para salir.")
    t0 = time.time()
    tiempo_ultima_mano = time.time()

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1) 
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
            
            tiempo_ms = int((time.time() - t0) * 1000)
            result = landmarker.detect_for_video(mp_image, tiempo_ms)

            if result.hand_landmarks:
                tiempo_ultima_mano = time.time()
                lm = result.hand_landmarks[0]
                
                accion, velocidad = decidir_movimiento(lm)
                texto = f"Gestos:  {accion} {velocidad}"

                h, w = frame.shape[:2]
                cv2.circle(frame, (int(lm[8].x * w), int(lm[8].y * h)), 12, (255, 0, 255), -1)
                
            else:
                tiempo_sin_mano = time.time() - tiempo_ultima_mano
                if tiempo_sin_mano > 0.1:
                    accion, velocidad = "stop", 0
                    texto = "FRENO JAEGER ACTIVADO"
                    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 10)
                else:
                    accion, velocidad = estado_actual
                    texto = "perdiendo señal..."

            if (accion, velocidad) != estado_actual:
                # Detenemos TODOS los motores siempre que cambiamos de acción
                motor_b.stop(brake=True)
                motor_c.stop(brake=True)
                motor_mediano.stop(brake=True)

                if accion == "avanzar":
                    motor_b.start_move(speed=velocidad, direction=1)
                    motor_c.start_move(speed=velocidad, direction=1)
                elif accion == "reversa":
                    motor_b.start_move(speed=velocidad, direction=-1)
                    motor_c.start_move(speed=velocidad, direction=-1)
                elif accion == "izquierda":
                    motor_b.start_move(speed=velocidad, direction=-1)
                    motor_c.start_move(speed=velocidad, direction=1)
                elif accion == "derecha":
                    motor_b.start_move(speed=velocidad, direction=1)
                    motor_c.start_move(speed=velocidad, direction=-1)
                    
                # Movimiento del motor mediano
                elif accion == "mediano_adelante":
                    motor_mediano.start_move(speed=velocidad, direction=1)
                elif accion == "mediano_atras":
                    motor_mediano.start_move(speed=velocidad, direction=-1)
                
                estado_actual = (accion, velocidad)

            cv2.putText(frame, texto, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.imshow("Landmarks EV3 (Gestos)", frame)

            if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q"), 27):
                break
                
    finally:
        motor_b.stop(brake=True)
        motor_c.stop(brake=True)
        motor_mediano.stop(brake=True)
        landmarker.close()
        cap.release()
        cv2.destroyAllWindows()
        brick.__exit__(None, None, None)
        print("Sistema desconectado con seguridad.")

if __name__ == "__main__":
    main()