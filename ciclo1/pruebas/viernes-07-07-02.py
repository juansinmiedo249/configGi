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

def ingresarEmpleado():
    while True:
        empleados = {}
        ced = leerInt("Ingrese el numero de la cedula:  ")
        nomb = leerStr("Ingrese el nombre del empleado:  ")    
        horas = leerHora("Ingrese la cantidad de horas laboradas:  ")
        vHora = leerValorHora("Ingrese el valor de la hora entre $8,000 y $150,000:  ")
        
        empleados[ced] = {}
        empleados[ced]["nombre"] = nomb
        empleados[ced]["horasTrabajadas"] = horas
        empleados[ced]["valorHora"] = vHora
        
        salBruto,eps,pension,salNeto = calSalario(vHora,horas)
        
        empleados[ced]["salBruto"] = salBruto
        empleados[ced]["eps"] = eps
        empleados[ced]["pension"] = pension
        empleados[ced]["salNeto"] = salNeto
        
        op = leerInt("Desea ingresar otro empleado \n  1. Si \n  2. No")
        if op == 2:
            break
    
    
    return empleados

def buscarEmpleado(dic):
    while True:
        nit = leerInt("Ingrese el nit del empleado:  ")
        for k in dic.keys():
            if nit == k:
                print("Se ha encontrado al empleado")
                print(f"Nombre : {dic[k]['nombre']} Cedula: {nit} ")
                op = leerInt ("¿Vas a modificar o eliminar? \n  1. Si \n  2.No")
                if op == 1:
                    return dic, nit
        print("!OOPS¡ No se encontro el nit qque ingresaste...")
    

def modificarEmpleado(dic,nit):
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
            dic[nit]["nombre"] = nNom
            print("Cambio realizado con exito")
        elif mod ==2:
            nHora = leerHora("Ingrese las horas trabajadas:  ")
            salBruto,eps,pension,salNeto = calSalario(nHora,dic[nit]["valorHora"])
            dic[nit]["horasTrabajadas"] = nHora
            dic[nit]["salBruto"] = salBruto
            dic[nit]["eps"] = eps
            dic[nit]["pension"] = pension
            dic[nit]["salNeto"] = salNeto
            print("Cambio realizado con exito")
        else:
            nVaHor = leerValorHora("Ingrese el valor de la hora entre $8,000 y $150,000:  ")
            salBruto,eps,pension,salNeto = calSalario(nVaHor,dic[nit]["horasTrabajadas"])
            dic[nit]["valorHora"] = nVaHor
            dic[nit]["salBruto"] = salBruto
            dic[nit]["eps"] = eps
            dic[nit]["pension"] = pension
            dic[nit]["salNeto"] = salNeto
            print("Cambio realizado con exito")
            
        opc = leerInt("Deseas hacer otra modificacion \n  1. Si \n  2. No\n")
        if opc == 2:            
            break
        
        
def eliminarEmpleado(dic,nit):
    n = dic[nit]["nombre"]
    dic[nit] = {}
    print(f"El empleado {n} con nit # {nit} ha sido eliminado exitosamente")
    print("Presione enter para continuar...")
        
        
def mostrarEmpleado(dic):
    nit = leerInt("Ingrese el numero de la cedula:  ")
    aux = 0
    if dic[nit]["salBruto"] > 1_160_000:
        aux = 140_606
    
    tPagar = dic[nit]["salNeto"] + aux
    
    print(f"Total a pagar al empleado {dic[nit]['nombre']} identificado con CC {nit}\n")
    print(f"Horas trabajadas: {dic[nit]['horasTrabajadas']}   Valor hora {dic[nit]['valorHora']}")
    print(f"Subtotal............${dic[nit]['salBruto']}")
    print(f"eps..................-${dic[nit]['eps']}")
    print(f"pension..............-${dic[nit]['pension']}")
    print(f"Auxilio.............+${aux}")
    print("                   ___________________________________")
    print(f"Total................${tPagar}")
    
    
    
def mostrarEmpleados(dic):
    
    for k in dic.keys():
        print(f"{dic[k]['nombre']}   nit   {dic[k]['horasTrabajadas']}   {dic[k]['valorHora']}")
        
        
def listarNomina(dic):
    pass
    
    
    
    
while True:
    op = menu()
    if op == 1:
        print("Agregar Empleado")
        lisEmpleados = ingresarEmpleado()
    elif op == 2:
        modificarEmpleado(buscarEmpleado(lisEmpleados))
    elif op == 3:
        buscarEmpleado(lisEmpleados)
    elif op ==4:
        eliminarEmpleado(buscarEmpleado(lisEmpleados))
    elif op == 5:
        mostrarEmpleados(lisEmpleados)
    elif op == 6:
        mostrarEmpleado(lisEmpleados)
    elif op == 7:
        pass
    elif op == 8:
        break
    else:
        print("Ingrese una opcion valida")
        print("Presione ENTER para continuar...")
        