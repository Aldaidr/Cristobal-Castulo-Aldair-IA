"""
EV3 — Ejemplo 5: dos motores avanzan (B y C)
"""
import time
import ev3_dc as ev3

with ev3.EV3(protocol=ev3.USB) as brick:
    izq = ev3.Motor(ev3.PORT_A, ev3_obj=brick, speed=45)
    der = ev3.Motor(ev3.PORT_C, ev3_obj=brick, speed=45)

    print("Avanzar...")
    izq.start_move(speed=45, direction=1)
    der.start_move(speed=45, direction=1)
    time.sleep(2.0)

    izq.stop(brake=True)
    der.stop(brake=True)

print("Listo.")