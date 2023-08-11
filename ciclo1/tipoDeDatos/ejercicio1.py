segundos = int(input("Ingrese la cantidad de segundos  "))

hora = segundos//3600

minutos = (segundos%3600)//60

segundos = (segundos%3600)%60

print("horas= ",hora)
print("minutos= ",minutos)
print("segundos= ",segundos)