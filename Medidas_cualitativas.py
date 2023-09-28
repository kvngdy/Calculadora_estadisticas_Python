from fractions import Fraction

def calcular_razon(a, b):
    if a == 0 or b == 0:
        return "No se puede calcular una fracción con denominador cero."

    return Fraction(a, b) 

def calcular_indice(razon):
    float(razon)
    
    return int(razon * 100)

def calcular_proporcion():
    print("\nProporcion\n")
    a = int(input("Ingresar el valor incial a comparar\n→ "))
    n = input("Ingresar todos los valores separados por una ','\n→ ")
    n = n.split(',')
    n = [int(numero) for numero in n]
    n = sum(n)
    
    return Fraction(a / n)#arreglao

def calcular_porcentaje():
    print("\nPorcentaje\n")   
    proporcion = calcular_proporcion()
    porcentaje = float(proporcion) * 100

    return "{:.2f}".format(porcentaje)