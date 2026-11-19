#El inventario de una tienda. Vas a guardar en una lista los productos de una tienda, a cada producto, le debes de guardar nombre, precio unitario y unidades que hay disponibles. 
#1.Tienes que imprimir el precio total de cada producto, es decir el total de todas las unidades de un producto. 
#2.Calcular el valor total del inventario. 
#3.Muestra los productos con menos de 5 unidades.
#4.Pregunta por un producto, si está en el diccionario, dile cuántas unidades hay, si no, dile que no existe
#5.Imprime cuál es el artículo más costoso



productos=[
    {"nombre": "Pan", "valor": 2500, "unidades": 40}, 
    
    {"nombre": "Arroz libra", "valor": 2000, "unidades": 10},

    {"nombre": "Huevos panal", "valor": 22500, "unidades": 12},

    {"nombre": "Mantequiella en barra", "valor": 3000, "unidades": 15},
    
    {"nombre": "Arepas x 5", "valor": 7000, "unidades": 8},

    {"nombre": "Cerveza central sin pack", "valor": 11000, "unidades": 0},

    {"nombre": "Papas de limon personal", "valor": 3000, "unidades": 2},

    ]

inventario=0
conmayorcosto=0
producto_caro=""
alerta_inventario=5

for producto in productos:
    
    total= producto['valor']* producto['unidades']
    print(f"{producto['nombre']} tiene un total de inventario de ${total}")
    inventario=inventario+total

    if total > conmayorcosto:
        producto_caro=producto["nombre"]
        conmayorcosto=total

    if producto['unidades']<alerta_inventario:
        print(f"CUIDADO{producto['nombre']} tiene pocas unidades: {producto['unidades']}")


    
print("El valor total del inventario es de: ",inventario)

print("El producto mas costos es: ", producto_caro, "con un precio de $", conmayorcosto)

buscador=input("Digite el producto a consultar: ")

for producto in productos:
    if buscador.lower()== producto['nombre'].lower():
        print(producto)
    else:
        print("El producto no existe en el sistema :p")