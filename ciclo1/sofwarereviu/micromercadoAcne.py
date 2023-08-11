import json

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                print("Presione ENTER para continuar...")
                continue
            return n
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")


def menu():
    print("******** MICROMERCADO ACME ********")
    print("Bienvenidos...")
    while True:
        print("1. Pagar en caja")        
        print("2. Informe de ventas")
        print("3. Salir")
        try:
            m = leerInt("Ingrese una opcion  ")
            if m < 1 or m > 4:
                print("!ERROR¡. Ingrese una opcion valida")
                print("Presione ENTER para continuar...")
                continue
            else:
                return m
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")




def productos():

    productos = {1 : {"nombre" : "Leche", "valor" : 1_900, "iva" : 1},
                 2 : {"nombre" : "Pan", "valor" : 2_000, "iva" : 2},
                 3 : {"nombre" : "Arroz", "valor" : 3400, "iva" : 3},
                 4 : {"nombre" : "Aceite", "valor" : 20_000, "iva" : 1},
                 5 : {"nombre" : "Huevos", "valor" : 15_000, "iva" : 2},
                 6 : {"nombre" : "Harina", "valor" : 3_500, "iva" : 3},
                 7 : {"nombre" : "Lentejas", "valor" : 3_000, "iva" : 1},
                 8 : {"nombre" : "Salchichon", "valor" : 17_500, "iva" : 2},
                 9 : {"nombre" : "Chocolate", "valor" : 7_000, "iva" : 3},
                 10 : {"nombre" : "Cafe", "valor" : 12_000, "iva" : 1}
                 }
    return productos
    

# terminar el can
def calValor(can,valor,iv):
    
    iva = {1 : 0, 2 : 0.05, 3 : 0.19}
    if iv == 1:
        sub = valor * can
        impu = sub * iva[iv]
        vT = sub + impu
    elif iv == 2:
        sub = valor * can
        impu = sub * iva[iv]
        vT = sub + impu
    else:
        sub = valor * can
        impu = sub * iva[iv]
        vT = sub + impu
    return vT,impu, sub

        
def valiRepetir(msg):
    while True:
            entrada = 0
            try:
                entrada = leerInt(msg)
                if entrada < 1 or entrada > 2:
                    print("!ERROR¡. Ingrese una opcion valida.")
                    input("Presione ENTER para continuar...")
                    continue
                return entrada                
            except ValueError:
                print("!OOPS¡. Ubo un error inesperado en el programa")
                input("Presione ENTER para continuar...")
    

def imprimirFactura(ced,venta):
    
    subTotal = 0
    ivat = 0
    total = 0
    
   
    for k in venta[ced].keys():
                    
        vaToAr, ivaA, subAr = calValor(venta[ced][k]["cantidad"],venta[ced][k]["valor"],venta[ced][k]["iva"]) 
        print (f"{k}\t{venta[ced][k]['nombre']}\t{venta[ced][k]['cantidad']}\t{venta[ced][k]['valor']}\t\t{ivaA}\t{vaToAr}" )
        subTotal += subAr
        ivat += ivaA
        total += vaToAr
                    
            
    print(f"\n\n\t\t\t\tSubtotal\t${subTotal}")
    print(f"\t\t\t\t\Iva\t\t${ivat}")
    print("\t\t\t\t__________________")
    print(f"\t\t\t\tTotal\t\t${total}")
    input("Presione ENTER para continuar...")                    
 


def agreproducto(product,venta):
    
    count = [0,0,0,0,0,0,0,0,0,0]    
    while True: 
        ced = leerInt("Ingrese el nit del cliente:  ")
        venta[ced] = {}   
        while True:            
            op = leerInt("Ingrese el codigo del producto:  ")
            if op > 10:
                print("El producto no se encuentra registrado")
                input("Presione ENTER para continuar...")            
                continue
            
            venta[ced][op] = {}            
            venta[ced][op]["nombre"] = product[op]["nombre"]
            venta[ced][op]["valor"] = product[op]["valor"]
            venta[ced][op]["iva"] = product[op]["iva"]
            count[op-1] += 1
            entrada = valiRepetir("Desea ingresar otro producto \n  1. Si \n  2. No \n")
            if entrada == 2:
                for k in venta[ced].keys():
                    venta[ced][k]["cantidad"] = count[k-1]
                                   
                print(f"Cedula del cliente:\t{ced}")
                print("Codigo\tNombre\tCantidad\tValor Un.\tIva\tTotal")
                imprimirFactura(ced,venta)
                with open(ruta1,"w") as file:
                    json.dump(venta,file)
                break
        cli = valiRepetir("Desea ingresar otro cliente \n  1. Si \n  2. No \n")
        if cli == 2:
            break
            
def cargarInfo(ruta,dic):
    with open ( ruta,"a+") as file:
        file.seek(0)
        # Verificar datos
        try:
            dic = json.load(file)
        except Exception as e:
            dic ={}
    print(dic)
        

ruta1 = "juan/ciclo1/sofwarereviu/micromercadoAcneVentas.json"
ruta2 = "juan/ciclo1/sofwarereviu/micromercadoAcneInforme.json"
venta = {}
while True:
    cargarInfo(ruta1,venta)
    op = menu()
    if op == 1:
        produc = productos()
        agreproducto(produc,venta)
        
