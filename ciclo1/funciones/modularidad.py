# SINTAXIS

"""def nombreFuncion([param1,param2]):# Los corchetes es para indicar que los parametros es opcional
    cuerpoFuncion"""
    
# funcion que sumen 2 numeros

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
        

def suma(a,b):
    s = a + b
    return s

a = leerInt("Ingrese un numero:\n")
b = leerInt("Ingrese un numero:\n")
print(f"El resultado de la suma es:  {suma(a,b)}")