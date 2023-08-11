producto = float(input("Ingrese el valor del producto\n"))

iva=producto*0.15
totalProduc = producto + iva
descuento = 0
totalProducDes = 0

if totalProduc > 1000:
    descuento= totalProduc *0.05
    totalProducDes = totalProduc-descuento
    
else:
    totalProducDes = totalProduc-descuento
    
print(f"Producto....${producto}")
print(f"IVA.........${iva}")
print("           ________________")
print(f"Subtotal....${totalProduc}")
print(f"Descuento..$-{descuento}")
print("           ________________")
print(f"Total.......${totalProducDes}")