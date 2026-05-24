
1. ¿Qué es una variable en Python?

Una variable es un espacio en una memoria que almacena un valor y que puede cambiar durante la ejecucuin del programa.
en python,las variables pueden guardar distintos tipos de datos:

* Enteros(int) - numeros sin decimales.
* Flotante(float) - numeros con decimales
* Cadenas(str) - texto
* Booleanos(bool) - valores logicos true o false

Nombres Invalidos

- 2variable(no puede empezaar con numero)
- precio-total(no se permiten guiones)
- class(palabra reservada de python)

2. ¿Qué diferencia hay entre = y == en Python?

= - Asignacion: se usa para guarda un valor en una variable
== - Comparacion: se usa para verificar si dos valores son iguales.

x = 5   # asinga el valor 5 a la variable
y = 5

Print(x == y)  # true, porque x y y tienen el mismo valor

3. ¿Qué es la indentación en Python y por qué es importante?

La identacion es el uso de espacios o tabulaciones al inicio de las lineas de codigo para indicar que instrucciones pertenecen a un bloque (if,for,while.funciones)

if true:
print("Hola")  #Error:falta indentacion

if True:
    print("hola") # correcto

4. Diferencia entre ciclo for y ciclo while

for: se usa cuando sabes cuantas veces quieres repertir algo.
while: se usa cuando quiere repetir mientras se cumpla una condicion.

for ¡ in range(5):
     print(¡) # inprime 0,1,2,3,4

x = 0
while x < 5:
    print(x)
    x += 1   # imprime 0,1,2,3,4     

5. ¿Qué hace la función range() en Python?

range() genera una secuentacia de numeros enteros.Se usa comunmente en cliclos for.

* range(5) - genera 0,1,2,3,4 (empieza en 0, termina en 4)
* range(1,10) - genera ,1,2,3,4,5,6,7,8,9 (empíeza en 1, termina en 9)
* range(0,10,2) -  genera 0,2,4,6,8 (empieza en 0, termina en 8 incrementa de 2 en 2 )


