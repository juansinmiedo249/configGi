num = int(input("Ingrese un numero\n"))
numper = 0

for i in range (1,num):
    if num % i == 0:
        numper +=i
        
if num == numper:
    print(f"El numero {num} es perfecto")
else:
    print(f"El numero {num} no es perfecto")