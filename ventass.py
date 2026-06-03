import csv
from datetime import datetime
from pathlib import Path


def calcular_total(precio, cantidad):
    subtotal = precio * cantidad
    iva = subtotal * 0.16
    total = subtotal + iva
    return subtotal, iva, total


productos = []
total_general = 0

while True:
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad vendida: "))

    subtotal, iva, total = calcular_total(precio, cantidad)

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "subtotal": subtotal,
        "iva": iva,
        "total": total
    }

    productos.append(producto)
    total_general = total_general + total

    continuar = input("¿Agregar otro producto? si/no: ").lower()

    if continuar == "no":
        break


ticket = "----- TICKET DE VENTA -----\n"

for producto in productos:
    ticket = ticket + "-------------------------\n"
    ticket = ticket + f"Producto: {producto['nombre']}\n"
    ticket = ticket + f"Precio: ${producto['precio']:.2f}\n"
    ticket = ticket + f"Cantidad: {producto['cantidad']}\n"
    ticket = ticket + f"Subtotal: ${producto['subtotal']:.2f}\n"
    ticket = ticket + f"IVA: ${producto['iva']:.2f}\n"
    ticket = ticket + f"Total: ${producto['total']:.2f}\n"

ticket = ticket + "-------------------------\n"
ticket = ticket + f"TOTAL A PAGAR: ${total_general:.2f}\n"

print(ticket)


carpeta_tickets = Path("tickets")
carpeta_tickets.mkdir(exist_ok=True)

ahora = datetime.now()

fecha_archivo = ahora.strftime("%Y-%m-%d_%H-%M-%S")
fecha = ahora.strftime("%Y-%m-%d")
hora = ahora.strftime("%H:%M:%S")

nombre_archivo = carpeta_tickets / f"ticket_{fecha_archivo}.txt"

with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write(ticket)

print(f"El ticket se guardó en: {nombre_archivo}")


archivo_csv = Path("ventas.csv")
existe_archivo = archivo_csv.exists()

with open(archivo_csv, "a", newline="", encoding="utf-8") as archivo:
    columnas = ["fecha", "hora", "producto", "precio", "cantidad", "subtotal", "iva", "total"]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)

    if not existe_archivo:
        escritor.writeheader()

    for producto in productos:
        escritor.writerow({
            "fecha": fecha,
            "hora": hora,
            "producto": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": producto["cantidad"],
            "subtotal": producto["subtotal"],
            "iva": producto["iva"],
            "total": producto["total"]
        })

print("Las ventas también se guardaron en ventas.csv")