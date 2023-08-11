import re

contrasena = input("Ingrese una contraseña: ")

longitud_minima = len(contrasena) >= 8
tiene_minuscula = re.search('[a-z]', contrasena) is not None
tiene_mayuscula = re.search('[A-Z]', contrasena) is not None
tiene_numero = re.search('[0-9]', contrasena) is not None
no_contiene_espacios = ' ' not in contrasena
tiene_caracter_especial = re.search('[%^&]', contrasena) is not None

if longitud_minima and tiene_minuscula and tiene_mayuscula and tiene_numero and no_contiene_espacios and tiene_caracter_especial:
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")
 #if not (longitud_valida and contiene_minuscula and contiene_mayuscula and contiene_numero and no_contiene_espacios and contiene_caracter_especial):