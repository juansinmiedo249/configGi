"""EjercicioDadoelnombreyestrato(1,2,3,4,5)deunusuariodelserviciodeenergíaeléctrica,
calcularloquepagaríadetarifabásicadelserviciodeenergíaeléctrica,quedependedelestrato,
asíEstratoTarifaBásica
1$10.000
2$15.000
3$30.000
4$50.000
5$65.000
Sepidevisualizarelnombreytarifabásica"""

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 or n > 5:
                print("!ERROR¡. Ingrese un estrato valido (1-5)")
                input("Presione enter para continuar...")
                continue
            return n
        except Exception as e:
            print("!ERROR¡, ingrese el nombre. ", e.message)
            
def leerString(msg):
    while True:
        try:
            n = input(msg)
            if n.strip()=="":
                print("!ERROR¡. Ingrese un nombre valido (1-5)")
                input("Presione enter para continuar...")
                continue
            return n
        except ValueError:
            print("!ERROR¡, ingrese un numero valido")
            
            
def calTarifaBasica(est):
    if est == 1:
        return 10_000
    elif est == 2:
        return 15_000
    elif est == 3:
        return 30_000
    elif est == 4:
        return 50_000
    else:
        return 65_000

nombre = leerString("Ingrese el nombre:  ")
estrato = leerInt("Ingrese el estrato:  ")


tarifas = calTarifaBasica(estrato)

print(f"\n La tarifa del estrato {estrato} es:   ${tarifas:,}")