Programa:Practicando ciclos
Descripción:Practicando ciclos for y while
Autor: Sebastian Buitrago  
Fecha: 2026-05-14
ANIO_ACTUAL = 2026


print("===EJERCICIO 1: CONTAR NUMEROS===")
    for i in range(1, 6):
        print(f"contando: {i}")

print("\n===EJERCICIO 2: SUMA ACUMULATIVA===")
        suma = 0
        for numero in range(1, 11):
            suma += numero
            print(f"Suma acumulativa: {suma}")
            print(f"\nTotal final: {suma}")

print("\n===EJERCICIO 3: PEDIR NUMEROS===")
            contador = 0
            while contador < 5:
                numero = int(input(f"Dame el número {contador + 1}: "))
                print(f"Guardaste el número: {numero}")
                contador += 1

print("\n===EJERCICIO 4: NUMEROS PARES===")
        print("Números pares del 1 al 28:")
        for numero in range(1, 21):
            if numero % 2 == 0:
                print(numero, end=" ")
                print()

    