import json
import os.path

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


#verificacion que introduzca un entero
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


#verificacion que introduzca un string
def leerStr(msg):
    while True:
        try:
            nom = input(msg)
            if nom.isdigit() == True:
                print("!ERROR¡. Nombre no valido")
                print("Presione ENTER para continuar...")
                continue
            return nom
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")


# Funcion para ingresar las horas laboradas
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


#funcion para ingresar el valor de la hora
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


# Funcion para calcular el salario de cada empleado
def calSalario(vh,h):
    salBruto = vh * h
    eps = salBruto * 0.04
    pension = salBruto * 0.04
    salNeto = salBruto - eps - pension
    
    return salBruto,eps,pension,salNeto

def escribirDisco(dic):
    
    with open("emplacme.json", "w") as archivo:        
        for emple in dic:
            ingre = str(dic[emple])
            ingre = ingre.split(";") + "\n"
            json.dump(ingre,archivo)

    if not archivo.closed:
        print("Cerrando archivo")
        archivo.close()


def leerArchivo(ruta):
    try:
        with open(ruta, "r") as file:
            dicJson = json.load(file)
    except FileExistsError:
        dicJson = {}
    return dicJson
        

# Funcion para hacer el registro de un empleado nuevo
def ingresarEmpleado(dicJson):    
    empleados = {}
    
    while True:
        
        ced = leerInt("Ingrese el numero de la cedula:  ")
        nomb = leerStr("Ingrese el nombre del empleado:  ")    
        horas = leerHora("Ingrese la cantidad de horas laboradas:  ")
        vHora = leerValorHora("Ingrese el valor de la hora entre $8,000 y $150,000:  ")
        
        empleados[ced] = {}
        empleados[ced]["nombre"] = nomb
        empleados[ced]["horasTrabajadas"] = horas
        empleados[ced]["valorHora"] = vHora
        dicJson[ced] = {}
        dicJson[ced]["nombre"] = nomb
        dicJson[ced]["horasTrabajadas"] = horas
        dicJson[ced]["valorHora"] = vHora
        
        with open(ruta,"w") as file:
            json.dump(dicJson,file)
        
        
        salBruto,eps,pension,salNeto = calSalario(vHora,horas)
        
        empleados[ced]["salBruto"] = salBruto
        empleados[ced]["eps"] = eps
        empleados[ced]["pension"] = pension
        empleados[ced]["salNeto"] = salNeto
        input("Presione ENTER para continuar...")
        
        op = leerInt("Desea ingresar otro empleado \n  1. Si \n  2. No\n")
        if op == 2:
           
            break
    
    
    return empleados


# Funcion para realizar la busqueda de un empleado
def buscarEmpleado(dic):
    
    while True:
        try:
            encon = False
            nit = leerInt("Ingrese el nit del empleado:  ")                     
            for k in dic.keys():
                if nit == k:
                    print("Se ha encontrado al empleado\n")                                       
                    encon = True                                      
                    return  nit
            if encon == False:
                print("!OOPS¡ No se encontro el nit que ingresaste...")
                input("Presione ENTER para continuar...")
        except ValueError:
            print("!OOPS¡ No se encontro el nit que ingresaste...")




# Funcion para mostrar los datos de un empleado previamente buscado
def mostrarEmpleado(dic,nit):
    text = open("juan/ciclo1/softwareRewiu/emplacme.dat", "r+")
    text.write("\n\n3. Empleado Encontrado\n")
    sCed = str(nit)
    sHoras = str(dic[nit]["horasTrabajadas"])
    SVHora = str(dic[nit]["valorHora"])  
    print(dic[nit])
    print(f"nombre: {dic[nit]['nombre']}")
    print(f"nit: {nit}")
    print(f"Horas Trabajadas: {dic[nit]['horasTrabajadas']}")
    print(f"Valor de la hora: {dic[nit]['valorHora']}")
    imprimir = sCed+";"+dic[nit]["nombre"]+";"+sHoras+";"+SVHora
    text.write(imprimir+"\n")
    text.close()
    input("Presione ENTER para continuar...")
    

# Funcion para modificar los datos de un empleado previamente buscado
def modificarEmpleado(dic,nit,ruta):
    dicJson ={}
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
            
        for k in dic.keys():
            dicJson[k] = {}
            dicJson[k]["nombre"] = dic[k]["nombre"]
            dicJson[k]["horasTrabajadas"] = dic[k]["horasTrabajadas"]
            dicJson[k]["valorHora"] = dic[k]["valorHora"]
            
        with open(ruta,"w") as file:
            json.dump(dicJson,file)
            
        opc = leerInt("Deseas hacer otra modificacion \n  1. Si \n  2. No\n")
        if opc == 2:            
            break
        

# Funcion para eliminar los datos de un empleado previamente buscado        
def eliminarEmpleado(dic,nit):
    n = dic[nit]["nombre"]    
    dic.pop(nit)
    print(f"El empleado {n} con nit # {nit} ha sido eliminado exitosamente")
    input("Presione enter para continuar...")
        

# Funcion para mostrar la nomina de un empleado en espesifico        
def mostrarNominaEmpleado(dic,nit):    
    aux = 0
    if dic[nit]["salBruto"] < 1_160_000:
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
    input("Presione enter para continuar...")
    
    
# Funcion para mostrar los datod de los empleados    
def mostrarEmpleados(dic):
    itera = 5  
    for k in dic.keys():
        print(f"{dic[k]['nombre']}   {k}   {dic[k]['horasTrabajadas']}   {dic[k]['valorHora']}")
        itera -=1
        if itera == 0:
            op = leerInt("Deseas continuar.\n 1. Si \n 2. No \n")
            if op == 1:
                itera = 5
            elif op == 2:                
                input("Presione enter para continuar...")
                break
        
        
def listarNomina(dic):
    itera = 5
    nominaTotal = 0 
    print("\n\nEmpleado   nit   Sal. bruto    Eps   pension    Sal. neto   auxilio     Total")   
    for k in dic.keys():
        if dic[k]["salBruto"] < 1_160_000:
            aux = 140_606
            total = dic[k]["salBruto"] + aux
        else:
            aux = 0
            total = dic[k]["salBruto"] + aux 
            
        nominaTotal += total

        print(f"{dic[k]['nombre']}   {k}   {dic[k]['salBruto']}   {dic[k]['eps']}    {dic[k]['pension']}    {dic[k]['salNeto']}  {aux}    {total}")
        itera -=1
        if itera == 0:
            op = leerInt("Deseas continuar.\n 1. Si \n 2. No \n")
            if op == 1:
                itera = 5
            elif op == 2:                
                input("Presione enter para continuar...")
                break

    
ruta = "juan/ciclo1/sofwarereviu/emplacme.json" 
dicJson = leerArchivo(ruta)
while True:
    op = menu()
    if op == 1:
        print("Agregar Empleado")
        lisEmpleados = ingresarEmpleado(dicJson)
    elif op == 2:
        cc = buscarEmpleado(lisEmpleados)
        modificarEmpleado(lisEmpleados,cc,ruta)        
    elif op == 3:
        cc = buscarEmpleado(lisEmpleados)
        mostrarEmpleado(lisEmpleados,cc)
    elif op == 4:
        cc = buscarEmpleado(lisEmpleados)
        eliminarEmpleado(lisEmpleados,cc)
    elif op == 5:
        mostrarEmpleados(lisEmpleados)
    elif op == 6:
        cc = buscarEmpleado(lisEmpleados)
        mostrarNominaEmpleado(lisEmpleados,cc)
    elif op == 7:
        listarNomina(lisEmpleados)
    elif op == 8:
        print("Fin del programa")
        break
    else:
        print("Ingrese una opcion valida")
        input("Presione ENTER para continuar...")
        

