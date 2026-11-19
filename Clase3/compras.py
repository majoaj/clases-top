cantidad=int(input("¿cuantos valores quieres agregar a tu lista de comprar?: "))
compras=[]

for i in range(cantidad):
    item=input(f"ingrese la comprar numero {i+1}:")
    compras.append(item)

#lista de compras del usuario
print(compras)

#ordenar compras alfabeticamente
compras.sort()
print(compras)
print("tu numero de cosas a comprar fue")
print(len(compras))