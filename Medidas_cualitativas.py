from fractions import Fraction

def calcular_razon(a, b):
    if a == 0 or b == 0:
        return "No se puede calcular una fracción con denominador cero."

    a_s_b = Fraction(a, b)
    b_s_a = Fraction(b, a)

    return a_s_b , b_s_a

def calcular_indice(a_s_b , b_s_a):
    indice_a_s_b = "{:.2f}".format(float(a_s_b * 100))
    indice_b_s_a = b_s_a * 100
    
    return indice_a_s_b , indice_b_s_a

def calcular_proporcion(a,b):
    proporcion = Fraction(a / (a+b)) 
    
    return proporcion

def calcular_porcentaje(proporcion):
    
    porcentaje = float(proporcion) * 100
    porcentaje_decimal = "{:.2f}".format(porcentaje)

    return porcentaje_decimal