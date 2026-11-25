lista1= [{"nombre":"Ana", "id":"1090272715", "fecha_na": "23-02-2005"}, {"nombre": "Majo", "id":"No", "fecha_na":"No"}]



def lista(clientes):
    club_Daluzed=[]

    for cliente in clientes:

        if cliente['nombre'].lower() != "no" and cliente['id'].lower() != "no" and cliente['fecha_na'].lower() !="no":
            club_Daluzed.append(cliente['nombre'])

    return club_Daluzed

print(lista(lista1))      
