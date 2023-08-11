nombre = input("Ingrese nombre del empleado\n ")
salario = int(input("Ingrese el salario del empleado\n "))
subTrans=0

if salario <= 1200000:
    subTrans = 120000
    
print (f"Nombre:      {nombre}")
print(f"Salario:      {salario}")
print(f"Subsidio:     {subTrans}")