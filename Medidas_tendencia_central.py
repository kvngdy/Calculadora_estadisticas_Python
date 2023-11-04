from Distribucion_frecuencias import frecuencia_acumulda as F_ac 
# media aritmetica
def media_arictmetica(f, X):
    fX = []
    for posicion in range(len(f)):
        fX.append(f[posicion] * X[posicion])
    
    return sum(fX)/sum(f)

#mediana
def mediana_tab(f, X):
    f_total = sum(f)
    F = F_ac(f)
    for posicion in range(len(X)):
        if f_total/2 < F[posicion]:
            return X[posicion]
        elif f_total/2 == F[posicion]:
            return (X[posicion]+X[posicion+1])/2
        
def mediana_clas_dats(lim, f):
    F = F_ac(f)
    f_total = sum(f)
    for posicion in range(len(f)):
        if f_total/2 <= F[posicion]:
            return lim[posicion] + ((f_total/2 - F[posicion-(1 if posicion != 0 else 0)])/(F[posicion]-F[posicion-(1 if posicion != 0 else 0)]))*(lim[posicion+1]-lim[posicion])

# moda
def moda_tab(f, X):
    for posicion in range(len(X)):
        if max(f) == f[posicion]:
            return X[posicion]

def moda_clas_dats(lim, f):
    delta = 0 
    delta2 = 0
    for posicion in range(len(f)):
        if max(f) == f[posicion]:
            delta = f[posicion] - f[posicion-(1 if posicion != 0 else 0)]
            delta2 = f[posicion] - f[posicion+(1 if posicion != len(f) else 0)]
            return lim[posicion] + delta/(delta + delta2) * (lim[posicion+1]-lim[posicion])

# cuantiles
def cuantil_tab(f, X):
    f_total = sum(f)
    F = F_ac(f)
    cuantil_calcular = int(input('''
¿Que cuantil decea calcular?
1) Cuartiles
2) Deciles
3) Percentiles    
> '''))
    parte_cuantil = int(input('¿Que parte del cuantil decea calcular?\n> '))

    if cuantil_calcular == 1:
        cuantil_calcular = 4

    elif cuantil_calcular == 2:
        cuantil_calcular = 10

    elif cuantil_calcular == 3:
        cuantil_calcular = 100

    else:
        print("Error cuantil seleccionado no esta en las opciones vuelva a intar¡¡¡")
        exit()

    if parte_cuantil <= 0 or parte_cuantil >= cuantil_calcular:
        print("La parte a cualcular no puede ser menor a 1 ni mayor o igual al cuantil deceado a calcular, vuelva a intentarlo")
        exit()



    cuantil = (parte_cuantil * (f_total - 1))/cuantil_calcular + 1

    for posicion in range(len(f)):
        if int(cuantil) < F[posicion]:
            return X[posicion]
        elif int(cuantil) == F[posicion]:
            return X[posicion]+(cuantil- int(cuantil))*(X[posicion+(1 if posicion == len(f) else 0)] - X[posicion])

def cuantil_clas_dats(lim, f):
    f_total = sum(f)
    F = F_ac(f)
    cuantil_calcular = int(input('''
¿Que cuantil decea calcular?
1) Cuartiles
2) Deciles
3) Percentiles    
> '''))
    parte_cuantil = int(input('¿Que parte del cuantil decea calcular?\n> '))

    if cuantil_calcular == 1:
        cuantil_calcular = 4

    elif cuantil_calcular == 2:
        cuantil_calcular = 10

    elif cuantil_calcular == 3:
        cuantil_calcular = 100

    else:
        print("Error cuantil seleccionado no esta en las opciones vuelva a intar¡¡¡")
        exit()

    if parte_cuantil <= 0 or parte_cuantil >= cuantil_calcular:
        print("La parte a cualcular no puede ser menor a 1 ni mayor o igual al cuantil deceado a calcular, vuelva a intentarlo")
        exit()
    cuantil = (parte_cuantil * f_total)/cuantil_calcular

    for posicion in range(len(f)):
        if cuantil <= F[posicion]:
            return lim[posicion] + (cuantil - F[posicion-(1 if posicion != 0 else 0)])/(F[posicion]-F[posicion-(1 if posicion != 0 else 0)])* (lim[posicion+1]-lim[posicion])
