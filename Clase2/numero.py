usuario_num= int(input("digite la cantidad de numero que quiere: "))
mayor= 0

for i in range(usuario_num):
    num=int(input(f"ingrese el numero {i+1}:"))
    if mayor<=num:
        mayor=num
print("de los digitados, su numero mayor fue: ", mayor)