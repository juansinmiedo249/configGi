"""2. Búsqueda de palabra clave: Escribe un programa que solicite al usuario que ingrese una oración y una
palabra clave específica. El programa debe verificar si la palabra clave está presente en la oración y
mostrar un mensaje apropiado. Si la palabra clave se encuentra, el programa debe detenerse y mostrar
un mensaje de éxito. Si la palabra clave no se encuentra en la oración, el programa debe continuar
pidiendo al usuario que ingrese otra oración hasta que se encuentre la palabra clave o el usuario ingrese
"salir" para terminar el programa."""


palabraClave = input("Ingrese la palabra clave:\n")
entrar = True

while entrar == True:

    try:
        oracion = input("Ingrese una oracion\n")

        for i in oracion.split():
            if i.lower() == palabraClave.lower():
                print(f"¡FELICITACIONES! has usado la palabra clave {palabraClave} en la siguiente oracion: \n{oracion} ")
                entrar = False
                break
            else:
                print("Lo siento no has usado la palabra clave")

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        break


print("\n*******Fin del programa*******")