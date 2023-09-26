import Medidas_cualitativas as medidas
import Distribucion_frecuencias as df
from tabulate import tabulate



ingreso = input("Ingrese la lista de los datos serparados por una coma\n→ ")
lista = ingreso.split(',')
lista = [int(numero) for numero in lista]


if len(lista) > 20:
    print("\nSe ara la clasificacion de datos ")

    valores = df.calcular_valores(lista)
    intervalos = df.intervalos(valores)
    X = df.marca_clase(intervalos)
    f = df.frecuencia_intervalos(intervalos, lista)
    
else:
    #seleccion = input("Desea hacer operaciones B_asicas o T_ablas\n→ ")
    seleccion = "t"
    if seleccion[0] == "B" or seleccion[0] == "b":
        print("Se aran operaciones Basicas (Medidas cualitativas)")
        
    else:    
        print("Se ara la tabulacion discreta")
        X = df.tabulacion_discreta(lista)
        f = df.frecuencia(lista)


f_total = df.frecuencia_total(f)
h = df.frecuencia_relativa(f, f_total)
p = df.frecuencia_porcentual(h)
F = df.frecuencia_acumulda(f)
H = df.frecuencia_acumulda_relativa(F , f_total)
P = df.frecuencia_acumulada_porcentual(H)

f.append(f_total)

X.insert(0, "X")
f.insert(0, "f")
h.insert(0, "h")
p.insert(0, "p")
F.insert(0, "F")
H.insert(0, "H")
P.insert(0, "P")

datos = [X, f, h, p, F, H, P]

for i, fila in enumerate(datos):
    if i == 0:
        fila.append("Total")
    else:
        fila.append(" ")
    
datos_t = list(map(list, zip(*datos)))



print(tabulate(datos_t, headers="firstrow", tablefmt="grid"))