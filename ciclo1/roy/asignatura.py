def leerNota(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0 or n > 5:
                print("\n!ERROR¡. La nota tiene que estar en el rango de 0 a 5")
                input("Presione ENTER para continuar...")
                continue
            return n
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")

def ingresarNota(dic,lista):
    for i in range (len(lista)):
        nota = leerNota(f"Ingrese la nota de la asignatura {lista[i]}  ")
        dic[lista[i]] = nota

def mostrar(dic):
    print("\n**NOTAS**")
    for k in dic.keys():
        print(f"En {k} has sacado {dic[k]}")
        
def main():
    asignaturas = ("Matematicas", "Fisica", "Quimica", "Historia", "Lengua")
    notas = {}
    ingresarNota(notas,asignaturas)
    mostrar(notas)
    
main()