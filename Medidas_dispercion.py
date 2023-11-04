from Medidas_tendencia_central import media_arictmetica as media

def desviacion_media(f, X):
    XX = media(f, X)
    fXX =[]
    for posicion in range(len(f)):
        fXX.append(f[posicion]*(X[posicion] - XX))
        fXX[posicion] = -fXX[posicion] if fXX[posicion] < 0 else fXX[posicion]
    return sum(fXX)/sum(f)

def varianza(f, X):
    XX = media(f, X)
    fXX =[]
    for posicion in range(len(f)):
        fXX.append(f[posicion]*((X[posicion] - XX)**2))
    return sum(fXX)/(sum(f)-1)

def desviacion_estandar(f, X):
    return varianza(f,X) ** (1/2)

def coeficiente_variacion(f, X):
    return desviacion_estandar(f, X)/media(f, X) * 100


X = [2,3,4,5]
f = [10,16,13,11]
X = [44,52,60,68,76]
f = [2,4,8,6,4]
ejemplo = coeficiente_variacion(f, X)
print(ejemplo) 