nombre=input("Ingrese el nombre del estudiante\n")
notaCuan = int(input("Ingrese nota del estudiante en un rango de 0 a 100\n"))
notaCual=""

if notaCuan <=50:
    notaCual="D"
    
elif notaCuan <=79:
    notaCual="C"
    
elif notaCuan <=89:
    notaCual="B"
    
else:
    notaCual="A"
    
    
print(f"nombre:              {nombre}")
print(f"Nota cuantitativa:   {notaCuan}")
print(f"Nota cualitativa:    {notaCual}")