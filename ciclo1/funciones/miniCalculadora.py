
def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
            
def msgError(msg):
    print(f"--> !ERROR¡ {msg}")
    input("** presione cualquier tecla para continuar...")

def menu():
    while True:
        print("**MENU**\n")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Factorial")
        print("7. Salir")
        
        op = leerInt("\n Ingrese una opcion...")
        if op < 0 or op > 7:
            msgError("Opcion no valida")
            continue
        
        return op
            
        

def sumar():
    print("\n*** SUMAR ***\n")
    n1 = leerInt ("Ingrese un numero ")
    n2 = leerInt ("Ingrese un numero ")
    s = n1 + n2
    print (f"El  resultado de la suma es: {s}")
    input("** presione cualquier tecla para continuar...")

def restar ():
    print("\n*** RESTAR ***\n")
    n1 = leerInt ("Ingrese un numero")
    n2 = leerInt ("Ingrese un numero")
    r = n1 - n2
    print (f"El  resultado de la resta es: {r}")
    input("** presione cualquier tecla para continuar...")

def  multiplicar():
    print("\n*** MULTIPLICAR ***\n")
    n1 = leerInt ("Ingrese un numero")
    n2 = leerInt ("Ingrese un numero")
    m = n1 * n2
    print (f"El  resultado de la multiplicacion es: {m}")
    input("** presione cualquier tecla para continuar...")

def dividir():
    print("\n*** DIVIDIR ***\n")
    n1 = leerInt ("Ingrese un numero")
    n2 = leerInt ("Ingrese un numero")
    s = n1 / n2
    print (f"El  resultado de la division es: {s}")
    input("** presione cualquier tecla para continuar...")

def potencia():
    print("\n*** POTENCIA ***\n")
    n1 = leerInt ("Ingrese un numero")
    n2 = leerInt ("Ingrese un numero")
    s = n1 ** n2
    print (f"El  resultado de la potencia es: {s}")
    input("** presione cualquier tecla para continuar...")

def factorial():
    print("\n***FACTORIAL***\n")
    n = leerInt("Ingrese un numeo\n")
    f =1
    for i in range (1,n+1):
        f *= i
    print (f"El  resultado del factorial es: {f}")
    input("** presione cualquier tecla para continuar...")



while True:
    opcion = menu()
    
    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        dividir()
    elif opcion == 5:
        potencia()
    elif opcion == 6:
        factorial()
    elif opcion == 7:
        print("\n****Gracias por usar la mini calculadora")
        break
    else:
        msgError("opcion no valida")