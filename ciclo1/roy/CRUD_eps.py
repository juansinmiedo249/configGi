def leerStr(msg):
    while True:
        try:
            nom = input(msg)
            if nom.isdigit() == True:
                print("!ERROR¡. Nombre no valido")
                input("Presione ENTER para continuar...")
                continue
            return nom
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 :
                print("\n!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                input("Presione ENTER para continuar...")
                continue
            return n
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")


def menu():
    print("\n\n******** EPS ********")
    print("Bienvenidos...")
    while True:
        print("1. Ingrese un nuevo registro")
        print("2. Buscar un registro")        
        print("3. Modificar un registro")
        print("4. Eliminar un registro")        
        print("5. Mostrar todo")
        print("6. Salir")
        try:
            m = leerInt("Ingrese una opcion  ")
            if m < 1 or m > 6:
                print("!ERROR¡. Ingrese una opcion valida")
                input("Presione ENTER para continuar...")
                continue
            else:
                return m
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            input("Presione ENTER para continuar...")
            
            
def veriUsuario(lista,ced):
    for i in range(len(lista)):
            dic = lista[i]
            for k in dic.keys():
                if k == ced:
                    print("El usuario ya esta registrado")
                    input("Presione ENTER para continuar...")
                    return False
            
def nuevoRegistro(lista):
    usuario = {}
    cedula = leerInt("Ingrese el documento del usuario  ")
    verificacion = veriUsuario(lista,cedula)
    if verificacion == False:
        return
    nombre = leerStr("Ingrese el nombre del usuario  ")    
    edad = leerInt("Ingrese la edad de la persona  ")
    eps = leerStr("Ingrese el nombre de la EPS  ")
    usuario[cedula] = {}
    usuario[cedula]["nombre"] = nombre
    usuario[cedula]["edad"] = edad
    usuario[cedula]["eps"] = eps
    lista.append(usuario)
    
    
def buscarRegistro(lista,op):
    
    cedula = leerInt("Ingrese el numero de cedula del usuario  ")
    encontrado = False
    for i in range(len(lista)):
        dic = lista[i]
        for k in dic.keys():
            if k == cedula:
                encontrado = True
                print("Usuario encontrado")
                if op == 1:
                    print("Nombre\t\tDocumento\t\tEdad\t\tEPS")
                    print(f"{dic[k]['nombre']}\t\t{k}\t\t{dic[k]['edad']}\t\t{dic[k]['eps']}")
                    input("Presione ENTER para continuar...")
                elif op == 0:
                    return dic,i,cedula
    if encontrado == False:    
        print(f"El documento {cedula} no fue encontrado\n")
        input("Presione ENTER para continuar...")


def modificarRegistro(lista):
    print("\n Modificar Registro")
    dic,indice,cedula = buscarRegistro(lista,0)
    while True:
        print("1. Nombre")
        print("2. Edad")
        print("3. EPS")
        op = leerInt("Ingrese una opcion  ")
        
        if op == 1:
            nombre = leerStr("Ingrese el nombre del usuario  ")
            dic[cedula]['nombre'] = nombre
            print("modificacion exitosa")
        elif op == 2:
            edad = leerInt("Ingrese la edad de la persona  ")
            dic[cedula]['edad'] = edad
            print("modificacion exitosa")
        elif op == 3:
            eps = leerStr("Ingrese el nombre de la EPS  ")
            dic[cedula]['eps'] = eps
            print("modificacion exitosa")
        else:
            print("Opcion no valida intentelo nuevamente")
            input("Presione ENTER para continuar...")
            continue
        print("Deseas modificar otro dato  \n 1. Si  \n 2. No")
        opcion = leerInt("Ingrese una opcion  ")
        if opcion == 2:
            lista[indice] = dic
            break


def eliminarRegistro(lista):
    print("Eliminar Registro")
    dic,indice,cedula = buscarRegistro(lista,0)
    lista.pop(indice)
    print("Registro eliminado")
        
    
    
def mostrarTodo(lista):
    print("Nombre\t\tDocumento\t\tEdad\t\tEPS")
    for i in range (len(lista)):
        dic = lista[i]
        for k in dic.keys():
            print(f"{dic[k]['nombre']}\t\t{k}\t\t{dic[k]['edad']}\t\t{dic[k]['eps']}")
            
            
def main():
    personas = []
    while True:
        op = menu()
        if op == 1:
           nuevoRegistro(personas)
        elif op == 2 :
           buscarRegistro(personas,1)
        elif op == 3:
            modificarRegistro(personas)
        elif op == 4:
            eliminarRegistro(personas)
        elif op == 5:
            mostrarTodo(personas)
        elif op == 6:
            print("Fin del programa")
            break
        

main()