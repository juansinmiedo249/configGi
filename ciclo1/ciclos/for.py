#for i in range(5):
 #   print(i,"\n")
 
 
#for i in range (1,101):
 #   if i%2 == 0:
  #       print(i,end=", ")
  
  
"""numero =int(input("Ingrege un numero"))

multipli=1

for i in range (1,numero+1):
    multipli *= i
    
print(f"El factorial del numero {numero} es {multipli}")"""

numero = int(input("ingrese un numero"))
primo = True

for i in range(2,numero):
    if numero%i == 0:
        primo = False
        
if primo == True:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")