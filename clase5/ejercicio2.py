import pandas as pd

df = pd.read_csv(r"C:\Users\MAJO\Downloads\ventas_tienda.csv")

#print(df.head())
#print(df.tail(3))
#print(df.shape)
#print(df.columns)
#print(df.info())
print(df.describe())