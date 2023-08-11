miLista = []
print(miLista)
def buscarElement(lst,elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    return -1

miLista.append("alirio")
print(miLista)
miLista.append("carlos")
miLista.append("samuel")
miLista.append("daniel")
miLista.append("anfres")
miLista.append("juan")


pos = buscarElement(miLista,"juan")
print (pos)