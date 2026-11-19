numeros={
    "Ana": 3234030048,
    "Majo": 3145678909,
    "Isa": 3125678909
}

estudiante={
    "Nombre": "Majo",
    "Edad": "20 años",
    "Carrera": "Administración"
}

print(numeros["Ana"])

print(estudiante["Edad"])


for clave, valor in estudiante.items():
    print(f"La estudiante: {valor}")
    


productos= [
    {"nombre": "Pan", "valor": 2500, "Peso": 12}, 
    
    {"nombre": "Arroz", "valor": 3000, "Peso":30}
    
    ]
print(len(productos))