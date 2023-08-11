import io

#abrirlo
fd = open("juan/ciclo1/archivos/texto.txt","r",encoding="utf-8")
fd.seek(53)
#leer = fd.read()
leer2 = fd.readline()
#leer3 = fd.readlines()

fd.close()

print(leer2)