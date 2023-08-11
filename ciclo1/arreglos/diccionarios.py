diccionarioCategoria = {1:25000, 2:30000, 3:40000, 4:45000, 5:60000}

totHonor = 0
docentes = {}

while True:
    cedula = int(input("Ingrese la cedula del docente:  "))
    nombre = input("Ingrese el nombre del docente:  ")
    categoria = int(input("Ingrese la categoria del docente:  "))
    horas = int(input("Ingrese las horas laboradas del docente:  "))
    docentes[cedula] = {}
    docentes[cedula]["nombre"] = nombre
    docentes[cedula]["categoria"] = categoria
    docentes[cedula]["horas"] = horas
    
    opc = int(input("Deseas agregar otro docente \n 1. Si \n 2. No \n"))
    if opc == 2:
        break
    
print("\n\n *** INFORME ***")
print("=" * 30)
for k in docentes.keys():
    h = docentes[k]["horas"] * diccionarioCategoria[docentes[k]["categoria"]]
    totHonor += h
    print(docentes[k]["nombre"], f" -- ${h:,}")
print("=" * 30)
print(f"Total de honorarios de los docentes:  ${totHonor}")
