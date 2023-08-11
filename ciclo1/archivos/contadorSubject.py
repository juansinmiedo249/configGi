import io

fd = open("juan/ciclo1/archivos/mbox-short.txt", "r", encoding="utf-8")
con = 0
for linea in fd:
    
    if "Subject" in linea:
        con += 1

    
fd.close()

print(f"El documento tiene {con} lineas que contengan Subject")