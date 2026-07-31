"""
EV3 + MediaPipe — Control avanzado por landmark de la muñeca (USB).

RETOS SUPERADOS: 
- Zona muerta (0.35 - 0.65) para avanzar recto.
- Más lejos = más rápido (velocidad dinámica de 30 a 80).
- Dos motores (B y C) con giros estilo tanque.
- Seguridad "Jaeger": si se pierde la mano por 1 segundo, freno de emergencia.
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

# Usaremos dos puertos para los motores
PUERTO_IZQ = ev3.PORT_A
PUERTO_DER = ev3.PORT_C

# ---------------------------------------------------------------------------
# decidir_movimiento(x)
# Entrada: x de la muñeca (0.0 .. 1.0)
# Salida: (accion, velocidad) -> accion="avanzar"|"izquierda"|"derecha"|"stop"
# ---------------------------------------------------------------------------
def decidir_movimiento(x: float) -> tuple[str, int]:
    # 1. ZONA MUERTA (Centro): Avanzar recto sin temblar
    if 0.35 <= x <= 0.65:
        return ("avanzar", 40)
    
    # 2. GIRO IZQUIERDA: Si la mano está muy a la izquierda
    elif x < 0.35:
        # Calcular velocidad: Si está cerca de 0.35 -> vel 30. Si está cerca de 0 -> vel 80.
        # (0.35 - x) nos da una distancia. Lo dividimos entre 0.35 para sacar un porcentaje (0.0 a 1.0).
        porcentaje_distancia = (0.35 - x) / 0.35
        velocidad = 30 + (porcentaje_distancia * 50)
        return ("izquierda", int(velocidad))
    
    # 3. GIRO DERECHA: Si la mano está muy a la derecha
    else: # x > 0.65
        # Calcular velocidad: Si está cerca de 0.65 -> vel 30. Si está cerca de 1.0 -> vel 80.
        porcentaje_distancia = (x - 0.65) / 0.35
        velocidad = 30 + (porcentaje_distancia * 50)
        return ("derecha", int(velocidad))


def main() -> None:
    if not MODELO.exists():
        raise FileNotFoundError(f"Falta el modelo: {MODELO}")

    # Conectar EV3 y definir LOS DOS MOTORES
    brick = ev3.EV3(protocol=ev3.USB)
    motor_b = ev3.Motor(PUERTO_IZQ, ev3_obj=brick)
    motor_c = ev3.Motor(PUERTO_DER, ev3_obj=brick)
    
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

    print("EV3 Jaeger Listo. Mueve la mano. Q para salir.")
    t0 = time.time()
    
    # Variable para el RETO DE SEGURIDAD
    tiempo_ultima_mano = time.time()

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1) # Espejo para que sea intuitivo
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
            
            tiempo_ms = int((time.time() - t0) * 1000)
            result = landmarker.detect_for_video(mp_image, tiempo_ms)

            # Lógica de detección y seguridad
            if result.hand_landmarks:
                # Hay mano, actualizamos el tiempo de seguridad
                tiempo_ultima_mano = time.time()
                lm = result.hand_landmarks[0]
                x = lm[0].x
                accion, velocidad = decidir_movimiento(x)
                texto = f"x={x:.2f}  {accion} {velocidad}"

                # Dibujar un punto en la muñeca (landmark 0)
                h, w = frame.shape[:2]
                cv2.circle(frame, (int(x * w), int(lm[0].y * h)), 12, (0, 255, 0), -1)
                
            else:
                # No hay mano. Verificamos si pasó más de 1 segundo
                tiempo_sin_mano = time.time() - tiempo_ultima_mano
                if tiempo_sin_mano > 0.1:
                    accion, velocidad = "stop", 0
                    texto = "FRENO JAEGER ACTIVADO"
                    # Un efecto visual rojo para saber que se activó la seguridad
                    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 10)
                else:
                    # Mantenemos la última acción mientras esperamos a ver si vuelve la mano
                    accion, velocidad = estado_actual
                    texto = "perdiendo señal..."

            # Aplicar a los motores solo si cambió el estado
            if (accion, velocidad) != estado_actual:
                if accion == "stop" or velocidad == 0:
                    motor_b.stop(brake=True)
                    motor_c.stop(brake=True)
                elif accion == "avanzar":
                    # Ambos adelante
                    motor_b.start_move(speed=velocidad, direction=1)
                    motor_c.start_move(speed=velocidad, direction=1)
                elif accion == "izquierda":
                    # Motor izquierdo atrás, derecho adelante
                    motor_b.start_move(speed=velocidad, direction=-1)
                    motor_c.start_move(speed=velocidad, direction=1)
                elif accion == "derecha":
                    # Motor izquierdo adelante, derecho atrás
                    motor_b.start_move(speed=velocidad, direction=1)
                    motor_c.start_move(speed=velocidad, direction=-1)
                
                estado_actual = (accion, velocidad)

            # Dibujar textos y rectángulos guía
            cv2.putText(frame, texto, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            
            # Dibujar la "Zona Muerta" (0.35 a 0.65) en pantalla
            w = frame.shape[1]
            cv2.line(frame, (int(w * 0.35), 0), (int(w * 0.35), frame.shape[0]), (255, 255, 0), 2)
            cv2.line(frame, (int(w * 0.65), 0), (int(w * 0.65), frame.shape[0]), (255, 255, 0), 2)

            cv2.imshow("Landmarks EV3 (Jaeger)", frame)

            if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q"), 27):
                break
                
    finally:
        # Freno de seguridad final asegurando ambos motores
        motor_b.stop(brake=True)
        motor_c.stop(brake=True)
        landmarker.close()
        cap.release()
        cv2.destroyAllWindows()
        brick.__exit__(None, None, None)
        print("Sistema desconectado con seguridad.")

if __name__ == "__main__":
    main()