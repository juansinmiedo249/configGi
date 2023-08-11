def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n <= 0:
                print("!ERROR¡. Ingrese un estrato valido tiene que ser mayor a 0")
                input("Presione enter para continuar...")
                continue
            return n
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
            
            
def leerString(msg):
    while True:
        try:
            n = input(msg)
            if n.strip()=="":
                print("!ERROR¡. Ingrese un nombre valido ")
                input("Presione enter para continuar...")
                continue
            return n
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
            
            
def leerProgramaAcademico():
    while True:
        print ("¿A cual programa academico deseas aplicar?")
        print ("1. Técnico en Sistemas")
        print ("2. Técnico en Desarrollo de videojuegos")
        print ("3. Técnico en Animación Digital")        
        try:
            p = int(input())
            if p < 1 or p>3:
                print("!ERROR¡. Ingrese un estrato valido tiene que ser entre (1-3)")
                input("Presione enter para continuar...")
                continue
            return p
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
            
            
def leerBeca():
    while True:
        print ("¿Que tipo de beca tienes?")
        print ("1. Becapor rendimiento académico.")
        print ("2. Beca Cultural - Deportes.")
        print ("3. Sin Beca.")        
        try:
            b = int(input())
            if b < 1 or b > 3:
                print("!ERROR¡. Ingrese un estrato valido tiene que ser entre (1-3)")
                input("Presione enter para continuar...")
                continue
            return b
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
    
def  calMatricula(promAcad,beca):
    if promAcad == 1:
        promAcad = 800_000
    elif promAcad == 2:
        promAcad = 1_000_000
    else:
        promAcad = 1_200_000
        
    if beca == 1:
        beca = 0.5
    elif beca == 2:
        beca == 0.4
    else:
        matricula = promAcad
        
    matricula = promAcad * beca
    
    return matricula
    

cod = leerInt("Ingrese el codigo:  ")
nom = leerString("Ingresar el nombre del estudiante")
promAcad = leerProgramaAcademico()
beca = leerBeca()
valNetoPagar = calMatricula(promAcad,beca)


print("\n","-"*40)
print(f"El valor de la matricula del estudiante {nom} es:   ${valNetoPagar:,.0f}")