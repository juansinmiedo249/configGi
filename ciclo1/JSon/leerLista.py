import json

with open("juan/ciclo1/JSon/crearListaJson.json", "r") as archivo:
    lista = json.load(archivo)
    
if not archivo.closed:
    print("Cerraste el archivo")
    archivo.close()
    
print("Cerraste el archivo")

for i in lista:
    print(i,end=", ")
    
print("\n")