
usuario="majo"
contraseña="majo0328"
i=0

while True:
    u=input("digite su usuario: ")
    c=input("digite su contraseña: ")

    if usuario==u and contraseña==c:
        print("Acceso concedido")
        break
    elif i==2:
            print("ACCESO DENEGADO")
            break
    elif usuario!=u and contraseña!=c:
        i=i+1
        print("Acceso negado, te quedan: ",2-i,"intentos.")