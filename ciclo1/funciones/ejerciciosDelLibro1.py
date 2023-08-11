"""Diseñar una funcion que calcule la metia de tres numeros leidos del teclado y poner
 un ejemplo de su aplicacion"""
 
def media(n1,n2,n3):
    m = (n1+n2+n3)/3
    
    return m

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
            
a = leerInt ("Ingrese el primer numero") 
b = leerInt ("Ingrese el segundo numero")   
c = leerInt ("Ingrese el tercer numero")      

prom = media (a,b,c)
print(f"La media de los numeros {a}, {b}, {c} es {prom:.2f}")