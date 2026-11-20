#lista de notas del usuario, devolver si pierde o gana la materia

def lista_notas(notas):
    nota_minima=int(input("¿Cual es la nota minima para pasar la materia? "))
    promedio= sum(notas)/len(notas)
    paso= nota_minima <= promedio
    return paso

notas= [3,4,5,3,4]

print(lista_notas(notas))