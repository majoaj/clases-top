def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

altura=int(input("Cual es la altura del triangulo?"))
base=int(input("Cual es la base del triangulo?"))

print(area_triangulo(base,altura))

