empleados = []

def menu():
    print("******** NOMINA ACME ********")
    print("Bienvenidos...")
    while True:
        print("MENU")
        print("1- Agregar empleado")
        print("2- Modificar empleado")
        print("3- Buscar empleado")
        print("4- Eliminar empleado")
        print("5- Listar empleados")
        print("6- Listar nómina de un empleado")
        print("7- Listar nómina de todos los empleados")
        print("8- Salir")
        try:
            m = int(input("Ingrese una opcion  "))
            if m < 1 or m > 8:
                print("!ERROR¡. Ingrese una opcion valida")
                print("Presione ENTER para continuar...")
                continue
            else:
                return m
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")


def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                print("Presione ENTER para continuar...")
                continue
            return n
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")


def leerStr(msg):
    while True:
        try:
            nom = int(input(msg))
            if nom.isdigit() == True:
                print("!ERROR¡. Nombre no valido")
                print("Presione ENTER para continuar...")
                continue
            return nom
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")

def leerHora(msg):
    while True:
        try:
            h = int(input(msg))
            if h < 1 or h > 160:
                print("!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                print("Presione ENTER para continuar...")
                continue
            return h
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")


def leerValorHora(msg):
    while True:
        try:
            vH = int(input(msg))
            if vH < 8000 or vH > 150000:
                print("!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                print("Presione ENTER para continuar...")
                continue
            return vH
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")

def calSalario(vh,h):
    salBruto = vh * h
    eps = salBruto * 0.04
    pension = salBruto * 0.04
    salNeto = salBruto - eps - pension
    
    return salBruto,eps,pension,salNeto




def agregarEmpleado():
    empleado = []
    ced = leerInt("Ingrese el numero de la cedula:  ")
    nomb = leerStr("Ingrese el nombre del empleado:  ")    
    horas = leerHora("Ingrese la cantidad de horas laboradas:  ")
    vHora = leerValorHora("Ingrese el valor de la hora entre $8,000 y $150,000:  ")

    empleado.append(ced)
    empleado.append(nomb)    
    empleado.append(horas)
    empleado.append(vHora)

    salBruto,eps,pension,salNeto = calSalario(vHora,horas)
    empleado.append(salBruto)
    empleado.append(eps)    
    empleado.append(pension)
    empleado.append(salNeto)

    empleados.append(empleado)
    


def buscarEmpleado(id):
    for i in range(0,len(empleados)):
        for j in range (0):
            if empleados[i][j]  == id:
                return empleados[i], i
            
        print(f"No se encontro ningun empledo con el siguiente nit {id}")
        print("Presione ENTER para continuar...")


def modificarEmpleado(emple,pos):
    while True:
        print("Modificar empleado")
        print("1. Nombre")
        print("2. Horas trabajadas")
        print("3. Valor hora\n")
        try:
            mod = leerInt("Ingrese una opcion:  ")
            if mod < 1 or mod > 3:
                print("!ERROR¡. Opcion no valida intente nuevamente")
                print("Presione ENTER para continuar...")
                continue
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")

        if mod == 1:
            nNom = leerStr("Ingrese el nuevo nombre:  ")
            emple[1] = nNom
            print("Cambio realizado con exito")
        elif mod ==2:
            nHora = leerHora("Ingrese las horas trabajadas:  ")
            salBruto,eps,pension,salNeto = calSalario(nHora,emple[3])
            emple[2] = nHora
            emple[4].append(salBruto)
            emple[5].append(eps)    
            emple[6].append(pension)
            emple[7].append(salNeto)
            print("Cambio realizado con exito")
        else:
            nVaHor = leerValorHora("Ingrese el valor de la hora entre $8,000 y $150,000:  ")
            salBruto,eps,pension,salNeto = calSalario(nHora,emple[4])
            emple[3] = nVaHor
            emple[4].append(salBruto)
            emple[5].append(eps)    
            emple[6].append(pension)
            emple[7].append(salNeto)

        opc = leerInt("Deseas hacer otra modificacion \n  1. Si \n  2. No\n")
        if opc == 2:
            empleados[pos] = emple
            break


def mostrarEmpleado(emp):
    for i in range(0,3):
        print(emp[i],end="  ")

def eliminarEmpleado(msg):
    emple,pos=buscarEmpleado(leerInt(msg))
    nomb = emple[1]
    empleados.remove(empleados[pos])
    print(f"El empleado {nomb} ha sido eliminado")
    print("Presione ENTER para continuar...")

def mostrarEmpleados():
    
    for i in range (0,len(empleados)):
        for j in range (0,3):
            print(empleados[i][j], end="  ")
        if (i+1) % 5 == 0:
            most = leerInt("Deseas continuar \n  1. Si \n  2.No\n")
            if most == 2:
                print("Presione ENTER para continuar...")
                break

    
def calAuxilio(msg):
    emp,pos = buscarEmpleado(leerInt(msg))
    if emp[4] > 1160000:
        pass
        



while True:
    op = menu()
    if op == 1:
        print("Agregar Empleado")
        agregarEmpleado()
    elif op == 2:
        empl,pos = buscarEmpleado(leerInt("Ingrese el nit del empleado a modificar  "))
        modificarEmpleado(empl,pos)
    elif op == 3:
        mostrarEmpleado(buscarEmpleado(leerInt("Ingrese el nit del empleado  ")))
    elif op ==4:
        eliminarEmpleado("Ingrese el nit del empleado a eliminar")
    elif op == 5:
        mostrarEmpleados()
    elif op == 6:
        break