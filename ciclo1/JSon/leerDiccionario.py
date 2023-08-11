import json

with open("juan/ciclo1/JSon/diccionarioJeison.json","r") as archivo:
    dic = json.load(archivo)
    
if not archivo.closed:
    print("Cerraste el archivo")
    archivo.close()
    
print("Cerraste el archivo")

print(f"Diccionario:  {dic}")
print(dic["influencers"][0]["name"])