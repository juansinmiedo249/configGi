a = float(input("Ingrese el primer lado\n"))
b = float(input("Ingrese el segundo lado\n"))
c = float(input("Ingrese el tercer lado\n"))

p = (a+b+c)/2

if p > a  and  p > b  and  p > c:
    
    area = p*(p-a)*(p-b)*(p-c)
    area = area**0.5
    print(f"El area del triangulo es {area}")
    
else:
    print("No es un triangulo")
    
