def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("\n!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                input("Presione ENTER para continuar...")
                continue
            return n
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")
            
def leerStr(msg):
    while True:
        try:
            nom = input(msg)
            if nom.isdigit() == True or nom =="":
                print("!ERROR¡. Nombre no valido")
                input("Presione ENTER para continuar...")
                continue
            return nom
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            
def valiNombre(lista,nom):
    for k in lista.keys():
        if nom == k:
            print("El contacto ya esta registrado")
            input("Presione ENTER para continuar...")
            return False
    return True


def valiRepe(msg):
    while True:
        try:
            i = leerInt(msg)
            if i < 1 or i > 2:
                print("!ERROR¡. Ingrese una opcion valida")
                input("Presione ENTER para continuar...")                
                continue
            return i
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            input("Presione ENTER para continuar...")

def agregarContacto(lista):
    while True:
        nombre = leerStr("Ingrese el nombre:  ")
        val = valiNombre(lista,nombre)
        if val == True:
            tel = leerInt("Ingrese su Telefono:   ")
            lista[nombre] = tel
        op = valiRepe("Deseas agregar otro contacto.\n 1. Si \n 2. No\n")
        if op == 2:
            break
        
def mostrar(lista):
    print("\n**LISTA DE CONTACTOS**")
    for k in lista.keys():
        print(f"Nombre: {k}      Telefono: {lista[k]}")
        

def main():
    contactos = {}
    agregarContacto(contactos)
    mostrar(contactos)
    
    
main()
    
    