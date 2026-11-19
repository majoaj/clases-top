rellenos=["Maracuyá", "Milo", "Fresa", "Durazno", "Limón"]

relleno_len=len(rellenos)

print(len(rellenos))

print(rellenos[2])

print(rellenos[relleno_len-1])

print(rellenos[1:4])

print(rellenos)

#Modificar

#nuevo_relleno= input("Ingrese el nuevo relleno: ")
#rellenos.append(nuevo_relleno)

#print(rellenos)

#relleno_eliminar= input("Ingresa el relleno que quieras eliminar: ")
#rellenos.remove(relleno_eliminar)

print(rellenos)

rellenos[0]="Fresa"
print(rellenos)

rellenos[2]="Maracuyá"
print(rellenos)

rellenos.sort()
print(rellenos)

print("Mango" in rellenos)
    

for relleno in rellenos:
    print(relleno)