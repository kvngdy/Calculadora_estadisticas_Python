import matplotlib.pyplot as plt
from seaborn import barplot 

def Histograma(X, f):
    
    f = f[1:-2]
    X = X[1:-1]

    plt.title("Histograma")
    plt.ylabel("Frecuencia")
    plt.xlabel("X")
    barplot(x=X, y=f)
    plt.show()
        
def Poligono_frecuencias(X, f):
    f = f[1:-2]    
    X = X[1:-1]
    
    plt.title("Poligono de frecuencias")
    plt.ylabel("Frecuencia")
    plt.xlabel("X")

    diferencia = X[1]-X[0]
    f = [0] + f + [0]
    X = [X[0] - diferencia] + X + [X[-1] + diferencia ]
    
    plt.plot(X, f)    
    plt.plot(X, f, "o", color="red")
    for x, f in zip(X, f):
        plt.text(x, f, f"{x} , {f}", ha='center', va='bottom')
    plt.show()
      
def Ojiva(X, F):
    F = F[1:-1]    
    X = X[1:-1]
    
    plt.title("Ojiva")
    plt.ylabel("Frecuencia acumulada")
    plt.xlabel("X")

    diferencia = X[1]-X[0]
    F = [0] + F 
    X = [X[0] - diferencia] + X 
    
    plt.plot(X, F)
    plt.plot(X, F, "o", color="red")  
    
    for x, f in zip(X, F):
        plt.text(x, f, f"{x} , {f}", ha='center', va='bottom')
    
    plt.show()

def Ojiva_porcentual(X, P):
    P = P[1:-1]
    X = X[1:-1]
    
    plt.title("Ojiva porcentual")
    plt.ylabel("Frecuencia acumulada porcentual")
    plt.xlabel("X")
    
    diferencia = X[1]-X[0]
    P = [0] + P
    X = [X[0] - diferencia] + X 
    
    plt.plot(X, P)
    plt.plot(X, P, "o", color="red")

    for x, f in zip(X, P):
        plt.text(x, f, f"{x} , {f}%", ha='center', va='bottom')
    
    plt.show()
