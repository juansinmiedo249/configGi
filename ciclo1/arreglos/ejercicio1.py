def leerLetra(msg):
    while True:
        try:
            l = input (msg)
            if l.isdigit == True:
                print("!ERROR¡. Ingrese una letra valida ")
                input("Presione enter para continuar...")
                continue
            return l
        except Exception as e:
            print("!ERROR¡, ingrese una nota valida")
            
            
            
lsLetras = []
lsContador = [0,0,0,0,0]

while True:
    letra = leerLetra("Ingrese una letra:  ")
    letra = letra.lower()
    lsLetras.append(letra)
    op = int(input("Deseas ingreras otra letra. \n 1. Si \n 2. No "))
    if op == 2:
        break
    
lsContador[0] = lsLetras.count("a")
lsContador[1] = lsLetras.count("e")
lsContador[2] = lsLetras.count("i")
lsContador[3] = lsLetras.count("o")
lsContador[4] = lsLetras.count("u")

print(f"\n Ingresaste {lsContador[0]} veces la vocal a")
print(f" Ingresaste {lsContador[1]} veces la vocal e")
print(f" Ingresaste {lsContador[2]} veces la vocal i")
print(f" Ingresaste {lsContador[3]} veces la vocal o")
print(f" Ingresaste {lsContador[4]} veces la vocal u")
    