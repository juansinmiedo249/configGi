import io

fd = open("juan/ciclo1/archivos/mbox-short.txt", "r", encoding="utf-8")
con = 0
for linea in fd:
    linea = linea.rstrip()
    if not "@uct.ac.za" in linea:
        continue
    print(linea)
        

    
fd.close()

#print(f"El documento tiene {con} lineas que empiezan con From")