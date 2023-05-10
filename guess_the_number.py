from random import *

"""
if you can make this in a Django Project it would be super cool! 😮‍💨 🫠
👍🏻
"""

numero_secreto = 5  # randint(1, 100)
intentos = 8

nombre_usuario = input("> ¿Cúal es tu nombre?: ")

while intentos >= 0 or intentos <= 8:
    respuesta_usuario = input(f"""\n{nombre_usuario} estoy pensando en un número entre el 1 y el 33 👹
Intenta adivinarlo (tienes {intentos} intentos): """)
    respuesta_usuario_int = int(respuesta_usuario)


    if respuesta_usuario_int < 1 or respuesta_usuario_int > 100:
        intentos = intentos - 1
        print(f"""\n{respuesta_usuario_int} esta fuera de rango! Intenta denuevo.""")

    elif intentos == 1:
        print(f"\nPerdiste :( El numero secreto era {numero_secreto}")
        break

    elif respuesta_usuario_int < numero_secreto:
        intentos = intentos - 1
        print(f"""\nRespuesta incoreccta, {respuesta_usuario_int} es menor al número secreto. Intenta denuevo.""")

    elif respuesta_usuario_int > numero_secreto:
        intentos = intentos - 1
        print(f"""\nRespuesta incorrecta, {respuesta_usuario_int} es mayor al número secreto. Intenta denuevo.""")

    elif respuesta_usuario_int == numero_secreto:
        print(f"\nCorrecto ! {respuesta_usuario_int} es el número secreto! Felicidades 🎊!\nAdivinaste en {-intentos  +8} intentos.")
        break

'''
intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cuál es el número?: "))
    intentos += 1

    if estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")
'''
