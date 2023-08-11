"""Contador de vocales: Crea un programa que solicite al usuario ingresar una frase y cuente la cantidad
total de vocales en ella. Utiliza un ciclo "while" para recorrer cada letra de la frase. Si una vocal es
encontrada, incrementa el contador de vocales. Sin embargo, si el usuario ingresa la letra 'q', el programa
debe terminar y mostrar la cantidad total de vocales encontradas hasta ese momento."""

frase = input("\n Ingrese una frase que no contenga la letra q:\n")
contVocal = 0
entrada = True

while entrada == True:

    
        for i in frase.lower():
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                contVocal +=1  
            if i == "q":
                print("\n !00PS¡ Hemos encontrado la letra q en la oracion \nSe da por terminafo el programa")
                break
                                      

        print(f"En la frase {frase} se encontraron {contVocal}")
        entrada = False
