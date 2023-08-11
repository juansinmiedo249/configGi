import json

lista = [10,20,30,40,60]

with open("juan/ciclo1/JSon/crearListaJson.json", "w") as archivo:
    json.dump(lista,archivo)
    print("se ha escrito el archico")
    
if not archivo.closed:
    print("Cerraste el archivo")
    archivo.close()
    
print("Cerraste el archivo")