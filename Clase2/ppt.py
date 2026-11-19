i1=0
i2=0

while True:
    j1=input("escoja piedra, papel o tijera: ")
    j2=input("escoja piedra, papel o tijera: ")

    if j1==j2:
        print("Empate, jugar de nuevo")

    elif j1 == "tijera" and j2 == "piedra":
        print("gana jugador 2")
        i2=i2+1

    elif j1 == "tijera" and j2 == "papel":
        print("gana jugador 1")
        i1=i1+1

    elif j1 == "papel" and j2 == "piedra":
        print("gana jugador 1")
        i1=i1+1

    elif j1 == "papel" and j2 == "tijera":
        print("gana jugador 2")
        i2=i2+1

    elif j1 == "piedra" and j2 == "papel":
        print("gana jugador 2")
        i2=i2+1

    elif j1 == "piedra" and j2 == "tijera":
        print("gana jugador 1")
        i1=i1+1
        
    print("Puntuacion: Jugador 1: ", i1 ,"y jugador 2: ", i2)

    if i2==3:
        print("Gana jugador 2 por numero rondas")
        break
    elif i1==3:
        print("Gana jugador 1 por numero rondas")
        break
    else:
        print("continuen jugando")

    