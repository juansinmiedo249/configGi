import json


def nuevoJson(dic,ruta2):
    newDic = {}
    newDic["cliente"] = []
    
    for i in range(len(dic["cliente"])):
        customer = dic["cliente"][i]
        print(customer)
        if customer["Saldo"] > 35_000_000:
            newDic["cliente"].append(customer)
    with open(ruta2,"w") as file:
        json.dump(newDic,file,indent=4)

def cargarInfo(ruta1):
    with open(ruta1,"r") as file:
        dic = json.load(file)
    return dic


def main():
    ruta1 = "ciclo1/roy/Ahorradores.json"
    ruta2 = "ciclo1/roy/losMasAhorradores.json"
    clientes = cargarInfo(ruta1)
    nuevoJson(clientes,ruta2)

main()
        