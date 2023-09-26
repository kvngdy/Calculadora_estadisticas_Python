from math import sqrt as raiz
from math import ceil as redondeo


def tabulacion_discreta(lista):
    tabulacion = list(set(lista))
    return tabulacion

def frecuencia(lista):
    tabulacion = tabulacion_discreta(lista)
    f = {}

    for numero in lista:
        if numero in f:
            f[numero] += 1
        else:
            f[numero] = 1

    frecuencias_ordenadas = [f[numero] for numero in tabulacion]

    return frecuencias_ordenadas

def frecuencia_total(f):
    return sum(f)


def frecuencia_relativa(f, f_t):
    
    f_relativa = []
    
    numero = 0
    while numero != len(f):
        f_relativa.append(float("{:.2f}".format(f[numero] / f_t)))
         
        numero += 1
        precision = 2
        f_relativaR = [round(numero, precision) for numero in f_relativa]
        
    f_relativa.append(1)
  
    return f_relativa
    

def frecuencia_porcentual(f_r):
    f_porcentual = []
    
    for numero, valor in enumerate(f_r):
        f_porcentual.append(int(valor * 100))
    
    return f_porcentual

def frecuencia_acumulda(f):
    
    f_acumulda = []
    
    numero = 0
    while numero != len(f):
        if numero == 0:
            f_acumulda.append(f[numero])
        else:
            f_acumulda.append(f[numero] + f_acumulda[numero-1])
        
        numero += 1
    return f_acumulda    

def frecuencia_acumulda_relativa(f_a, f_t):    
    f_acumulda_relativa = []
    
    
    for numero in f_a:
        f_acumulda_relativa.append(float("{:.2f}".format(numero / f_t)))
    
    return f_acumulda_relativa    

def frecuencia_acumulada_porcentual(f_a_r):
    
    f_acumulada_porcentual = []
    
    for numero in f_a_r:
        f_acumulada_porcentual.append(int(numero * 100)) 
    
    return f_acumulada_porcentual 

#para listas que superen los 20 caracteres

def calcular_valores(lista):
    Xmax = max(lista)
    Xmin = min(lista)
    R = Xmax - Xmin
    K = redondeo(raiz(len(lista)))
    C = redondeo(R / K)

    if C * K > R:
        print("\nCumplio no se hace nada extra la diferencia es", C)

    else:
        C += 1
        d = K * C - R
        Xmin = redondeo(Xmin - (d / 2))  
        print("\nNo cumplio procedemos a hacer la otra manera difrerencia fue", C)
        
    return {
        "Xmax": Xmax,
        "Xmin": Xmin,
        "C": C
    }

def intervalos(valores):
    
    i = [valores["Xmin"]]
    num = 0
    while max(i) < valores["Xmax"]:
        i.append(i[num]+valores["C"])
        num += 1
    print("\n Li - Ls")
    for numero in range(len(i) - 1):
        print(i[numero], "-", i[numero + 1])

    return i


def marca_clase(intervalos):
    intervalos    
    x = []
    for numero in range(len(intervalos) - 1):
        x.append(int((intervalos[numero] + intervalos[numero +1]) / 2))    
    return x

def frecuencia_intervalos(intervalos,lista):
    f = [0] * (len(intervalos) - 1)

    for numero in lista:
        for i, (inicio, fin) in enumerate(zip(intervalos[:-1], intervalos[1:])):
            if inicio <= numero < fin:
                f[i] += 1

    return f
