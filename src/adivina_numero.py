Programa: Adivina el número
Descripcion: Juego en el que el usuario intenta adivinar un número generado aleatoriamente.
Autor: Sebastian Buitrago
fecha: 2026-05-15


NUMERO_SECRETO = 42
MAX_INTENTOS = 5

print("¡Bienvenido al juego de adivinar el número!")
print(f"Tienes {MAX_INTENTOS} intentos para adivinar el número SECRETO ")

intentos = 0
adivina = False 

while intentos < MAX_INTENTOS and not adivina:  
    numero = int(input(f"Intento {intentos+1}: Ingresa un número: "))
    intentos += 1

    if numero == NUMERO_SECRETO:
        print("¡Felicidades! Has adivinado el número.")
        adivina = True
    elif numero < NUMERO_SECRETO:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

if not adivina:
    print(f"Lo siento, no adivinaste el número. El número secreto era {NUMERO_SECRETO}.")

    