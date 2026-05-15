Programa: Hola Mundo Interactivo
Descripcion: Programa que saluda al usuario y muestra un menu de opciones
Autor: Sebastian Buitrago
fecha: 2026-05-14


NOMBRE_PROGRAMA= " Hola Mundo Interactivo"
VERSION= "1.0"
MAX_INTENTOS= 3
ANIO_ACTUAL= 2026





print("=" * 50)
print(f"{NOMBRE_PROGRAMA} v{VERSION}")
print("=" * 50)
print()

nombre_usuario= input("martina")

if nombre_usuario =="":
    print("No ingresaste un nombre. Te llamaré 'Usuario'.")
    nombre_usuario= "Usuario"
    else:
    print(f"¡Hola, {nombre_usuario}! Bienvenido al programa.")
print()

edad = int(edad_texto)
if edad < 18:
    print(f"Eres menor de edad, {nombre_usuario}.")
    categoria ="joven"
    elif edad >= 18 and edad < 60:
        print(f"Eres un adulto, {nombre_usuario}.")
        categoria ="adulto"
    else:
        print(f"Eres un adulto mayor, {nombre_usuario}.")
        categoria ="adulto mayor"

anio_nacimiento = ANIO_ACTUAL - edad
print(f"Naciste aproximadamente en el año  {anio_nacimiento}.")
print()

print("=" * 50)
print("MENU DE OPCIONES")
print("=" * 50)
print("1. ver tu informacion")
print("2. contar del 1 al 10")
print("3. Tabla de multiplicar")
print("4. Salir")
print("=" * 50)

continuar = True
intentos_fallidos = 0

while continuar:
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        print("\n--- TU INFORMACION ---")
        PRINT(f"Nombre: {nombre_usuario}")
        print(f"Edad: {edad} años")
        print(f"Categoria: {categoria}")
        print(f"Año de nacimiento: {anio_nacimiento}")
        intetnos_fallidos =0

    elif opcion == "2":
        print("\nContando del 1 al 10:")
        for numero in range(1, 11):
            print(f"Numero: {numero}"")
        intentos_fallidos =0

        elif opcion == "3":
            numero_tabla = input("\n¿ DE qye numero quieres la ttabla ?)
            numero_tabla = int(numero_tabla)
            print(f"\nTabla de multiplicar del {numero_tabla}:")
            for i in range(1, 11):
                resultado = numero_tabla * i
                print(f"{numero_tabla} x {i} = {resultado}")
            intentos_fallidos =0

    elif opcion == "4":
        print(f"\n¡Hasta luego, {nombre_usuario}!")
        print("Gracias por usar el programa.")
        continuar = False
    else:
        intentos_fallidos = intentos_fallidos + 1
        print(f"\nOpcion invalida.Intentos fallidos: {intentos_fallidos}/{MAX_INTENTOS}")
        if intentos_fallidos >= MAX_INTENTOS:
            print("Demasiados intentos fallidos. Cerrando el programa.")
            continuar = False

            Print("\n" + "=" * 50)
            print("PROGRAMA FINALIZADO") 
            print("=" * 50)
            
            
                       