import io

fd = open("juan/ciclo1/archivos/mbox-short.txt", "r", encoding="utf-8")

email = set()
for i in fd:
    if i.startswith("From:"):
        i = i[6:]
        email.add(i)
        
enviar = list(email)

text = open("juan/ciclo1/archivos/prueba.txt", "w")
for i in range (len(enviar)-1,0,-1):
    enviar[i] = enviar[i].rstrip()
    x = enviar [i] + "\t Enviado  OK"
    
    print(x)
    
    text.write(x+"\n")
    
    
    
    
                
text.close                

    
fd.close()

