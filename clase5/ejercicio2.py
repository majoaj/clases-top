import pandas as pd

df = pd.read_csv(r"C:\Users\MAJO\Downloads\ventas_tienda.csv")

#print(df.head())
#print(df.tail(3))
#print(df.shape)
#print(df.columns)
#print(df.info())
#print(df.describe())


#df[df["producto"]=="Café"]
#total_cafe=["cantidad"].sum()
#print(total_cafe)

#print((df["producto"]=="Café").value_counts())


filtro_producto = df[df["producto"] == "Café"] 
total_unidades = filtro_producto["cantidad"].sum() 

print(f"Total de unidades vendidas de café: {total_unidades}")

filtro_ciudad_pago=(df["ciudad"] == "Cali") & (df["metodo_pago"].isin(["Tarjeta","Transferencia"]))

cali= df[filtro_ciudad_pago]

print("Metodo de pago en la ciudad de cali",cali["metodo_pago"].value_counts())

cantidad= df["cantidad"]>=8
ventas_mayores=df[cantidad]
resultado=len(ventas_mayores)
print(f"Ventas con 8 unidades o más: {resultado}")


filtro_categoria=(df["categoria"] == "Papelería") & (df["cantidad"]>=8)
papeleria=df[filtro_categoria][["fecha","producto","cantidad","ciudad"]]
print(papeleria)


df["total"]=df["cantidad"]*df["precio_unitario"]
bottom=df.sort_values("total").head(1)
print(bottom[["producto","total"]])