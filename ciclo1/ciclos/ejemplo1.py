def leerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0 or n > 5:
                print("!ERROR¡. Ingrese un estrato valido (0-5)")
                input("Presione enter para continuar...")
                continue
            return n
        except Exception as e:
            print("!ERROR¡, ingrese una nota valida")

lsNotas = []

for est in range (1,11):
    nota = leerFloat(f"Ingrese nota del estudiante #{est} ")
    lsNotas.append(nota)
    
notMen = min(lsNotas)
print(f"La nota menor es:  {notMen}")
notMay = max(lsNotas)
print(f"La nota mayor es:  {notMay}")

promNotas = sum (lsNotas)/10
print(f"El promedio es:  {promNotas}")

lsNotas.sort(reverse=True)
tresNotas = lsNotas[0:3]
print("Las tres mejores notas son:  ",",".join(tresNotas))