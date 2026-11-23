import csv

suma_total=0
valor_alto=0
producto_caro=""
ciudad_mayor = ""
fecha_mayor = ""

with open (r"C:\Users\MAJO\Downloads\ventas_tienda.csv", encoding="utf-8") as archivo:
    for fila in csv.DictReader(archivo):

        cantidad= int(fila["cantidad"])
        precio_unitario= int(fila["precio_unitario"])
        producto=(fila["producto"])
        ciudad = fila["ciudad"]
        fecha = fila["fecha"]

        total_venta= cantidad * precio_unitario
        suma_total=suma_total+total_venta

        if total_venta > valor_alto:
            producto_caro=producto
            valor_alto=total_venta
            fecha_mayor=fecha
            ciudad_mayor=ciudad
            

        print(producto,total_venta)

print("La venta total fue de: $", suma_total)
print(f"{producto_caro} fue el producto mas caro con un valor de ${valor_alto}, comprado en la ciudad de {ciudad_mayor} el {fecha_mayor}")


