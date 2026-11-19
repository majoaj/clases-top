num1=int(input("ingresa tu numero de inicio: "))
num2=int(input("ingresa tu numero de final: "))
suma=0
for i in range(num1,num2+1):
    suma=i+suma
print("el resultado de la suma de todos tus numero es: ",suma)