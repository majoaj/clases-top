dolar=3000.0
euro=4000.0

valor_pesos=float(input("ingrese el valor a convertir en dolares y euros "))

valor_euros= valor_pesos / euro
valor_dolares= valor_pesos / dolar

print("tus pesos a dolares serian: $", valor_dolares)
print("tus pesos a euros serian: $", valor_euros)