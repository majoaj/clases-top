# pedir cantidad notas a ingresar, calcular promedio de las notas, decir cuantas materias gano

cantidad_notas=int(input("dime cuantas notas quieres ingresar: "))
pasar_materia=int(input("¿Con cuanta nota pasas tu materia? "))

lista_notas=[]
suma=0
item=0

for i in range(cantidad_notas):
    notas=int(input(f"ingrese la nota numero {i+1}:"))
    lista_notas.append(notas)

for nota in lista_notas:
    suma=suma+nota
    
for nota in lista_notas:
    if nota>=pasar_materia:
        item=item+1


#sacar promedio y materias coronadas
promedio= suma/len(lista_notas)

print("TU promedio fue de: ", promedio)
print("Pasaste", item, "materias")


print(lista_notas)