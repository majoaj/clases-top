valor_cuenta=float(input("Valor a pagar por la cuenta "))
valor_propina=float(input("Cuanto sera tu porcentaje de propina "))


valor_real_propina= valor_cuenta * (valor_propina/100)

print("La propina sera de:", valor_real_propina)

valor_total_cuenta= valor_cuenta + valor_real_propina 

print("Total a pagar: ", valor_total_cuenta)