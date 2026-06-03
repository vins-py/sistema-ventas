productos = []
total_general = 0

while True:
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad vendida: "))

    subtotal = precio * cantidad
    iva = subtotal * 0.16
    total = subtotal + iva

    productos.append([nombre, precio, cantidad, subtotal, iva, total])

    total_general = total_general + total

    continuar = input("¿Agregar otro producto? si/no: ").lower()

    if continuar == "no":
        break

print("----- TICKET DE VENTA -----")

for producto in productos:
    print("-------------------------")
    print(f"Producto: {producto[0]}")
    print(f"Precio: ${producto[1]:.2f}")
    print(f"Cantidad: {producto[2]}")
    print(f"Subtotal: ${producto[3]:.2f}")
    print(f"IVA: ${producto[4]:.2f}")
    print(f"Total: ${producto[5]:.2f}")

print("-------------------------")
print(f"TOTAL A PAGAR: ${total_general:.2f}")