import random

num1 = random.randint(1,10)
ganador = ""
intenGanador = float("inf")
print("*****ADIVINA EL NUMERO*****\n")

oportunidades = random.randint(3,6)


while oportunidades > 0:

    nombre = input("\nIngrese su nombre\n")
    intentos = 1
    validacion = 1

    print(f"\n{nombre} cuentas con {oportunidades} oportunidades")
    
    while validacion ==1 :
        try:
            num2 = int(input("Ingrese un numero\n"))
            validacion = 2

        except ValueError:
            print("¡Error!. Debes ingresar un numero valido\n")

    if num2 < num1:
        print("\nEl numero es mayor sigue intentando\n")

    elif num2 > num1:
        print("\nEl numero es menor sigue intentando\n")
        
    while num1 != num2:
        intentos +=1
        validacion = 1
        oportunidades -=1
        
        print(f"\n{nombre} te quedan {oportunidades} oportunidades\n")
        
        
        while validacion ==1 :
            try:
                num2 = int(input("\nIngrese un numero\n"))
                validacion = 2

            except ValueError:
                print("\n¡Error!. Debes ingresar un numero valido\n")

        if num2 < num1:
            print("\nEl numero es mayor sigue intentando\n")

        elif num2 > num1:
            print("El numero es menor sigue intentando\n")

        if oportunidades == 0:
            print(f"\n{nombre} te quedaste sin oportunidades")
            print(f"El numero secreto es: {num1}\n" )
            break        

    if intentos < intenGanador and num1 == num2:
        ganador = nombre
        intenGanador = intentos

    validacion = 1

    while validacion ==1 :
        try:
            jugar = int(input("Quieres volver a jugar \n 1.SI\n 2.no\n"))
            validacion = 2
        except ValueError:
            print("¡Error!. Debes ingresar un numero valido\n")

    if jugar == 1:
        num1 = random.randint(1,101)
        oportunidades = random.randint(3,6)


print(f"\nEl ganador es {ganador} con {intenGanador} intentos\n")