Programa: Calculadora simple    
Descripcion: Calculadora simple que realiza operaciones básicas como suma, resta, multiplicación y división.
Autor: Sebastian Buitrago
fecha: 2026-05-15

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))  

print("\n===Menu de operaciones===")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Seleccione una operación (1-4): "))

if opcion == 1:
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif opcion == 2:
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif opcion == 3:
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida. Debe elegir una opción entre 1 y 4.")

    