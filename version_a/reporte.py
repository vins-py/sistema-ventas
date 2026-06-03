import pandas as pd

ventas = pd.read_csv("ventas.csv")

print("----- REPORTE GENERAL -----")
print(ventas)

print("----- TOTAL VENDIDO POR DÍA -----")
total_por_dia = ventas.groupby("fecha")["total"].sum()
print(total_por_dia)

print("----- PRODUCTOS VENDIDOS POR DÍA -----")
productos_por_dia = ventas.groupby(["fecha", "producto"])["cantidad"].sum()
print(productos_por_dia)