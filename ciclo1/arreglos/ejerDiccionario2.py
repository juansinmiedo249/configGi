notas = {1:0.3, 2:0.3, 3:0.4}
estudiantes = {}
promedio = 0

def calNota(dicEstudiantes, dicNotas):
    print("\n\n *** INFORME ***")
    print("=" * 30)
    for k in dicEstudiantes.keys():
        n1 = dicEstudiantes[k]["nota1"] * dicNotas[1]
        n2 = dicEstudiantes[k]["nota2"] * dicNotas[2]
        n3 = dicEstudiantes[k]["nota3"] * dicNotas[3]
        
        notaFinal = n1 + n2 + n3
        if notaFinal >= 3:
            estado = "Aprobo"
        else:
            estado = "Reprobo"
        print(f"La nota definitiva del estudiante", {estudiantes[k]["nombre"]} ,f" es {notaFinal}, {estado} el curso")

while True:
    codigo = int(input("Ingrese la codigo del estudiante:  "))
    nombre = input("Ingrese el nombre del estudiante:  ")
    nota1 = float(input("Ingrese la nota 1:  "))
    nota2 = float(input("Ingrese la nota 2:  "))
    nota3 = float(input("Ingrese la nota 3:  "))
    estudiantes[codigo] = {}
    estudiantes[codigo]["nombre"] = nombre
    estudiantes[codigo]["nota1"] = nota1
    estudiantes[codigo]["nota2"] = nota2
    estudiantes[codigo]["nota3"] = nota3
    
    opc = int(input("Deseas agregar otro estudiante \n 1. Si \n 2. No \n"))
    if opc == 2:
        break
    
calNota(estudiantes,notas)