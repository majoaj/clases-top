#piedra papel o tijera, con funcion y libreria random
#adivina numero, con libreria random

import random

puntos_jugador=0
puntos_aleatorio=0

def aleatorio():
    opciones=["piedra","papel","tijera"]
    return random.choice(opciones)

def ganador(jugador,computador):
    
    if jugador==computador:
        return "Empate, jugar de nuevo"

    elif jugador == "tijera" and computador == "piedra":
        return "gana computador"
        

    elif jugador == "tijera" and computador == "papel":
        return "gana jugador 1"
        

    elif jugador == "papel" and computador == "piedra":
        return "gana jugador 1"
        

    elif jugador == "papel" and computador == "tijera":
        return "gana computador"
        

    elif jugador == "piedra" and computador == "papel":
        return "gana computador"

    elif jugador == "piedra" and computador == "tijera":
        return "gana jugador 1"
    
    else:
        return "respuesta no valida"    
    

def puntos(puntos_jugador, puntos_aleatorio, resultado):

    if resultado == "gana jugador 1":
        puntos_jugador = puntos_jugador + 1

    elif resultado == "gana computador":

        puntos_aleatorio=puntos_aleatorio+1

    return puntos_jugador, puntos_aleatorio

while puntos_jugador < 3 and puntos_aleatorio < 3:

    jugador=input("Elija piedra, papel o tijera: ").lower()
    computador=aleatorio()

    print("Claudio eligio: ", computador)

    resultado=ganador(jugador,computador)

    print(resultado)

    puntos_jugador, puntos_aleatorio = puntos(
    puntos_jugador,
    puntos_aleatorio,
    resultado
)
    print("Puntuación es ", "jugador: ", puntos_jugador, "claudio: ", puntos_aleatorio)


if puntos_jugador == 3:
    print("Ganaste la partida")

elif puntos_aleatorio == 3:
    print("Claudio ganó la partida")

    