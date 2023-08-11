"""4. Hacer un programa que pida al usuario un texto como contraseña y el programa debe validar si es válida.
Una contraseña es válida si:
• Tiene una longitud mínima de 8 caracteres
• Debe contener una letra en minúscula
• Debe contener una letra en mayúscula
• Debe contener un número
• No puede contener espacios
• Debe tener por lo menos uno de los siguientes caracteres especiales (%^&)"""


entrar = True
import 

while entrar == True:
    contraseña = input("Ingrese una contraseña\n")
    contador =0
    mayuscula = False
    minuscula = 0
    numero = False
    caracter = False

    for i in contraseña:
        contador += 1

    

    if contador >= 8:
        for i in contraseña:
            if i.isupper():
                mayuscula = True
            else:
                print("La contraseña debe tener al menos 1 mayuscula\n")
                break
            
            if i.islower():
                minuscula += 1
                
                if minuscula == F

                else:
                    print("La contraseña debe tener al menos 1 minuscula\n")
                    break

            if i.isdigit():
                numero = True
            else:
                print("La contraseña debe tener al menos 1 numero\n")
                break

            if i != " ":
                numero = True
            else:
                print("La contraseña no debe tener espacios\n")
                break
            
            if i == "%" or i == "^" or i == "&":
                caracter = True
                continue
            else:
                print ("La contraseña debe tener al menos uno de estos caracteres %^&")
                break

    else:
        print ("La contraseña debe tener al menos 8 caracteres ")

    if  mayuscula == True and minuscula == True and numero == True and caracter == True and contador >= 8 :
        entrar = False
        print(f"\nLa contraseña {contraseña} fue asignada con exito\n") 

   


