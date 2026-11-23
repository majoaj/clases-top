import random

intentos=0
def aleatorio():
    return (random.randint(1,100))

numero_secreto = aleatorio()

while True:
    guess=int(input("Digita un numero del 1 al 100: "))
    intentos=intentos+1

    if guess==numero_secreto:
        print("Felicidades lo encontraste")
        print("Encontraste el numero en el intento numero: ", intentos)
        break
    
    elif guess>numero_secreto:
        print("Estas unos numero muy arriba")

    elif guess<numero_secreto:
        print("tu número es muy pequeño 7w7")

    else:
        print("sigue intentando :p")



    
