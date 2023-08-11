def leerString(msg):
    while True:
        try:
            n = input(msg)
            if n.strip()=="":
                print("!ERROR¡. Ingrese un nombre valido ")
                input("Presione enter para continuar...")
                continue
            n = n.lower()
            return n
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
            
def menu():
    while True:
        print("Bienvenido al programa de selector de logo")
        print("******MENU******")
        print("1. Ingrese el nombre de la empresa.")
        print("2. Obtener caracteres mas repetidos con su residencias.")
        print("3. Obtener el logo")
        print("4. salir")
        
def buscarRepetidas(cadena):
    cadena.sort()
    ca = ()
    resi = ()
    log = {}
    a = ""
    b = ""
    c = ""
    
    for i in range (0,len(cadena)):
        if cadena[i] not in ca:
            r = cadena.count(cadena[i])
            ca.append(cadena[i])
            resi.append(r)
            
    for i in range (3):
        n = max(resi)
        ind = resi.index(n)
        a = resi[ind]
        
        
            
