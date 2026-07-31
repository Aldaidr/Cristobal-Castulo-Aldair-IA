"""
EV3 — Ejemplo 4: prueba A, B, C y D (2 s cada uno)
Mira cuál motor se mueve y usa ese puerto en tus scripts.
"""
import time
import ev3_dc as ev3

PUERTOS = [
    ("A", ev3.PORT_A),
    ("B", ev3.PORT_B),
    ("C", ev3.PORT_C),
    ("D", ev3.PORT_D),
]

with ev3.EV3(protocol=ev3.USB) as brick:
    juke = ev3.Jukebox(ev3_obj=brick)
    for nombre, puerto in PUERTOS:
        print(f">>> Puerto {nombre}")
        juke.play_tone("c'", duration=0.15)
        try:
            with ev3.Motor(puerto, ev3_obj=brick, speed=60) as motor:
                motor.move_for(2.0, speed=60, brake=True)()
        except Exception as e:
            print(f"   (sin motor o error en {nombre}: {e})")
        time.sleep(0.3)

print("Fin de la prueba de puertos.")