import json

miDic = {1:"Lapiz",2:"Borrador",3:"Cuadernos",4:"Lapicero","valor":2500}

miDic2 = {
    "influencers": [
        {
            "name": "Jaxon",
            "edad": 42,
            "work at": "Teach News"
        },
        {
            "name": "Miller",
            "edad": 35,
            "work at": "It Day"
        }
    ]
}

with open("juan/ciclo1/JSon/diccionarioJeison.json","w") as archivo:
    #json.dump(miDic,archivo)
    json.dump(miDic2,archivo)
    print("se ha escrito el archico")
    
if not archivo.closed:
    print("Cerraste el archivo")
    archivo.close()
    
print("Cerraste el archivo")