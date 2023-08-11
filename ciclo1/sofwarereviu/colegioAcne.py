import json

#validar que lo que ingrese sea un numero entero
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

# Validar que lo que ingrese sea un String
def leerStr(msg):
    while True:
        try:
            nom = input(msg)
            if nom.isdigit() == True:
                print("\n!ERROR¡. Nombre no valido")
                input("Presione ENTER para continuar...")
                continue
            return nom
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")

# Validar que escoja M/F segun corresponda el sexo del alumno
def leerSexo(msg):
    while True:
        try:
            s = input(msg).upper()
            if s == "M" or s == "F":
                return s
            else:
                print("\n!ERROR¡. Opcion no valida")
                input("Presione ENTER para continuar...")
        except ValueError:
            print("\n!OOPS¡. Ubo un error inesperado en el programa")
            input("Presione ENTER para continuar...")

# Validar que ingrese el grado correspondiente al alumno
def leerGrado(msg):
    while True:
        try:
            g = leerInt(msg)
            if g < 1 or g > 5:
                print("\n!ERROR¡. Ingrese una opcion valida")
                input("Presione ENTER para continuar...")
                continue
            return g
        except ValueError:
            print("\n!OOPS¡. Ubo un error inesperado en el programa")

#  Validar si va a volver a repetir la ultima accion
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

# valida que sean validas las notas
def leerNota(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0 or n > 5:
                print("\n!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                input("Presione ENTER para continuar...")
                continue
            return n
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")


# Menu del programa
def menu():
    print("\n\n******** INSTITUTO EDUCATIVO ACME ********")
    print("Bienvenidos...")
    while True:
        print("1. Registrar alumno nuevo")
        print("2. Buscar estudiante")        
        print("3. Modificar datos del alumno")
        print("4. Eliminar alumno")
        print("5. Ingresar notas del alumno")
        print("6. Notas por grado")
        print("7. Top 5 mejores por grado")
        print("8. Top 5 mejores del la Institucion")
        print("9. Salir")
        try:
            m = leerInt("Ingrese una opcion  ")
            if m < 1 or m > 9:
                print("!ERROR¡. Ingrese una opcion valida")
                input("Presione ENTER para continuar...")
                continue
            else:
                return m
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            input("Presione ENTER para continuar...")

# Ingresar los datos al diccionario
def llenarDiccio(dic,nit,nom,sex,grado):
    dic[nit] = {}
    dic[nit]["nombre"] = nom
    dic[nit]["sexo"] = sex
    dic[nit]["grado"] = grado
    return dic

# Registrar un estudiante nuevo
def ingresarEstudiante(dic,ruta1):
    while True:
        print("\nRegistro de estudiante nuevo")
        nit = leerInt("Ingrese el numero de documento del alumno:  ")
        nom = leerStr("Ingrese el nombre del alumno:  ")
        sex = leerSexo("Ingrese el sexo del estudiante M/F:  ")
        grado = leerGrado("Ingrese el grado del alumno de 1 a 5:  ")
        dic = llenarDiccio(dic,nit,nom,sex,grado)

        with open(ruta1,"w") as file:
            json.dump(dic,file)
        op = valiRepe("Deseas registrar otro alumno. \n  1. Si \n  2. No\n")
        if op == 2:
            break

# Busca un estudiante por si id
def buscarEstudiante(estudiantes,mod=0):
    nit = str(leerInt("Ingrese el numero de documento del estudiante:  "))
    encontraso = False
    for k in estudiantes.keys():
        if nit == k:
            print("\nEstudiante encontrado")
            print(f"Nit      {k}")
            print(f"Nombre   {estudiantes[k]['nombre']}")
            print(f"Sexo     {estudiantes[k]['sexo']}")
            print(f"Grado    {estudiantes[k]['grado']}")
            encontraso = True
            input("Presione ENTER para continuar...")
            continue
    if encontraso == False:
        print("\nEstudiante no registrado")
        input("Presione ENTER para continuar...")
    if mod == 1:
        return k
    
# Modifica los datos de in estudiante mediante su id
def modificarEstudiante(estudiantes,ruta1):
    mod = 1
    nit =str(buscarEstudiante(estudiantes,mod))
    print("\nModificacion de estudiante")
    while True:
        print("1. Nombre")
        print("2. Sexo")
        print("3. Grado")
        x = leerInt("Digite una opcion:  ")
        if x < 1 or x > 3:
            print("!ERROR¡. Ingrese una opcion valida")
            input("Presione ENTER para continuar...")            
        if x == 1:
            nNom = leerStr("Ingrese el nuevo nombre del estudiante:  ")
            estudiantes[nit]["nombre"] = nNom
            print("\nModificacion realizada con exito")
        elif x == 2:
            nSex = leerSexo("Ingrese el nuevo sexo del estudiante:  ")
            estudiantes[nit]["sexo"] = nSex
            print("\nModificacion realizada con exito")
        else:
            nGrado = leerGrado("Ingrese el nuevo grado del estudiante: ")
            estudiantes[nit]["grado"] = nGrado
            print("\nModificacion realizada con exito")
        op = valiRepe("Deseas seguir modificando \n  1. Si \n  2. No")
        if op == 2:
            with open(ruta1,"w") as file:
                json.dump(estudiantes,file)
                print("\nNuevos datos del estudiante")
                print(f"Nit      {nit}")
                print(f"Nombre   {estudiantes[nit]['nombre']}")
                print(f"Sexo     {estudiantes[nit]['sexo']}")
                print(f"Grado    {estudiantes[nit]['grado']}")
            break
        

# Elimina un estudiante buscado por su id
def eliminarEstudiante(estudiantes,ruta1):
    mod = 1
    nit =str(buscarEstudiante(estudiantes,mod))
    nom = estudiantes[nit]['nombre']
    estudiantes.pop(nit)
    print(f"\nEl estudiante {nom} con documento #{nit} ha sido eliminado satisfactoriamente")
    input("Presione ENTER para continuar...")
    with open(ruta1,"w") as file:
        json.dump(estudiantes,file)

# calcular el promedio de cada alumno
def calPromedio(lista):
    x = len(lista) 
    prom = 0
    for i in range(len(lista)):
        prom += lista[i]
    prom /= x
    return prom


# Ingreso de notas por grado ordenando alfabeticamente el nombre de los alumnos
def ingresarNotas(estudiantes,ruta1):
    print("\n***Ingreso de notas***")
    while True:
        grado = leerGrado("Ingrese el grado a cual desees acceder.  ")
        estuOrd = dict(sorted(estudiantes.items(), key = lambda x: x[1]['nombre'])) # organiza el diccionario por nombres
        for k in estuOrd.keys():
            if estuOrd[k]["grado"] == grado:
                notas = []
                while True:
                    nota = leerNota(f"Ingrese nota del alumno {estuOrd[k]['nombre']} de (0 a 5):  ")
                    notas.append(nota)
                    print ("Nota ingresada")
                    op = valiRepe("Desea ingresar otra nota. \n  1. Si \n  2. No\n")
                    if op == 2:
                        estudiantes[k]["notas"] = notas
                        estudiantes[k]["promedio"] = calPromedio(estudiantes[k]["notas"])
                        with open(ruta1,"w") as file:
                            json.dump(estudiantes,file)
                        break
        op = valiRepe("Desea ingresar las notas de otro grado. \n  1. Si \n  2. No\n")
        if op == 2:
            break


def notasGrado(estudiantes):
    print("\n***Notas por grado***")
    while True:
        grado = leerGrado("Ingrese el grado a cual desees acceder.  ")
        estuOrd = dict(sorted(estudiantes.items(), key = lambda x: x[1]['promedio'], reverse=True)) #organiza por promedio
        print("\n")
        print(f"\nNotas del grado {grado}")
        for k in estuOrd.keys():
            if estuOrd[k]["grado"] == grado:
                print(f"nombre: {estudiantes[k]['nombre']}\tnotas: {estudiantes[k]['notas']}\tpromedio: {round(estudiantes[k]['promedio'],1)}")
        op = valiRepe("Desea ver las notas de otro grado. \n  1. Si \n  2. No\n")
        if op == 2:
            break


# muestra los 5 mejores estudiantes por grado
def excelenciaGrado(estudiantes):
    print("\n***Excelencia por grado***")
    print(f"\nCuadro de excelencia del grado {grado}")
    while True:
        grado = leerGrado("Ingrese el grado a cual desees acceder.  ")
        estuOrd = dict(sorted(estudiantes.items(), key = lambda x: x[1]['promedio'], reverse=True))
        print("\n")
        i = 0
        for k in estuOrd.keys():        
            if estuOrd[k]["grado"] == grado:
                print(f"nombre: {estudiantes[k]['nombre']}\tpromedio: {round(estudiantes[k]['promedio'],1)}")
                i += 1
            if i == 5:
                break
        op = valiRepe("Desea ver las notas de otro grado. \n  1. Si \n  2. No\n")
        if op == 2:
            break


# muestra los 5 mejores estudiantes de la institucion
def exelenciaInstucion(estudiantes):
    print("\n***Cuadro de excelencia de la institucion***")
    estuOrd = dict(sorted(estudiantes.items(), key = lambda x: x[1]['promedio'], reverse=True))
    print("\n")
    i = 0
    for k in estuOrd.keys():
        print(f"nombre: {estudiantes[k]['nombre']}\tgrado: {estudiantes[k]['grado']}\tpromedio: {estudiantes[k]['promedio']}") 
        i += 1
        if i == 5:
            break


# Carga un diccionario exixtente de lo contrario devuelve uno vacio
def cargarInfo(ruta):
    with open ( ruta,"a+") as file:
        file.seek(0)
        # Verificar datos
        try:
            dic = json.load(file)
        except Exception as e:
            dic ={}
        return dic


# Ejecucion del programa
def main():
    ruta1 = "juan/ciclo1/sofwarereviu/colegioAcneEtudiantes.json.py"    
    estudiantes = cargarInfo(ruta1)    
    
    while True:
        op = menu()
        if op == 1:
            ingresarEstudiante(estudiantes,ruta1)            
        elif op == 2:
            buscarEstudiante(estudiantes)
        elif op == 3:
            modificarEstudiante(estudiantes,ruta1)
        elif op == 4:
            eliminarEstudiante(estudiantes,ruta1)
        elif op == 5:
            ingresarNotas(estudiantes,ruta1)
        elif op == 6:
            notasGrado(estudiantes)
        elif op == 7:
            excelenciaGrado(estudiantes)
        elif op == 8:
            exelenciaInstucion(estudiantes)
        elif op == 9:
            break

    print("Fin del programa")

main()