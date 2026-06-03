producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad vendida: "))

subtotal = precio * cantidad
iva = subtotal * 0.16
total = subtotal + iva

if total >= 1000:
    descuento = total * 0.10
else:
    descuento = 0

total_final = total - descuento

print("----- TICKET DE VENTA -----")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA: ${iva:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Total final: ${total_final:.2f}")