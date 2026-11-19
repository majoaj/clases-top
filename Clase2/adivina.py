numero=78
i=0
while True:
    guess=int(input("Digita un numero del 1 al 100: "))
    i=i+1
    if guess==numero:
        print("Felicidades lo encontraste")
        print("Encontraste el numero en el intento numero: ", i)
        break
    elif guess>numero:
        print("Estas unos numero muy arriba")
    elif guess<numero:
        print("tu número es muy pequeño 7w7")

    else:
        print("sigue intentando :p")