Programa: Lista de compras  
Descripcion: Lista de compras con sus respectivos precios, cantidad y total a pagar y descuentos.
Autor: Sebastian Buitrago
fecha: 2026-05-15



cantidad = int(input("Cuantos productos vas a comprar: "))

total = 0

for i in range(cantidad):
    nombre = input(f"producto {i+1} - Nombre: ")
    precio = float(input(f"producto {i+1} - Precio: $")))
    total += precio

    if total > 100:
        descuento = total * 0.10
        total -= descuento
        print(f"\nSe aplico un 10% de descuento: (${descuento:.2f}).")

        print(f"\nEL total a pagar es: ${total:.2f}.")

