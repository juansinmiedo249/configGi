#5.Escribir un programa en el que a partir de una fecha introducida por teclado con el formato DIA-
#MES-AÑO, se obtenga la fecha del día siguiente.

#Para realizar el cálculo de forma correcta se debe tener en cuenta que hay meses con 30 días y otros
#con 31 y que febrero puede tener 29 si es bisiesto el año.}

dia = int(input("Ingrese el dia\n"))
mes = int(input("Ingrese el mes\n"))
año = int(input("ingrese el año\n"))

print(f"\n{dia}/{mes}/{año}")

if mes==1 or mes==3 or mes==5 or mes==7 or mes ==8 or mes==10 or mes==12:
    mesDia = 31

elif mes==2:
    mesDia=28
    if año%4==0 and año%400==0 or año%100!=0:
        mesDia=29

else:
    mesDia=30


dia += 1

if dia > mesDia:
    dia = 1
    mes +=1

if mes>12:
    mes = 1
    año += 1

print(f"{dia}/{mes}/{año}\n")   