Programa:Calculadora de edad
Descripción:Calculadora básica de edades.
Autor: Sebastian Buitrago  
Fecha: 2026-05-14
ANIO_ACTUAL = 2026


print("===CALCULADORA DE EDAD===")

nombre = input("tu nombre: ")
anio_nacimiento = int(input("año de nacimiento: "))

anio_nacimiento = int(anio_nacimiento)

edad = ANIO_ACTUAL - anio_nacimiento

print(f"\n Hola {nombre}, tienes : {edad} años.")

if edad >= 18:
    print("Eres mayor de edad.")
    else:
    print("Eres menor de edad.")
    anos_faltantes = 18 - edad
    print(f"Te faltan {anos_faltantes} años para ser mayor de edad.")
    