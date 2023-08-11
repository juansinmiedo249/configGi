hora = int(input("Ingrese la hora\n"))
minutos = int(input("Ingrese los minutos\n"))
segundos = int(input("Ingrese los segundos\n"))
jornada = int(input("1.AM \n2.PM\n"))

if jornada ==2 and hora != 12:
    hora = hora+12
    
if jornada == 1 and hora == 12:
    hora = 00

           
        
print (f"{hora}:{minutos}:{segundos}")

print(hora,":",minutos,":",segundos)