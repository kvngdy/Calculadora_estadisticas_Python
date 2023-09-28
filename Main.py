import Medidas_cualitativas as mc
import Distribucion_frecuencias as df
from tabulate import tabulate
import Graficar as gf

seleccion = input("""¿Qué operaciones desea realizar?
1) Medidas Cualitativas
2) Distribucion de frecuencias
→ 
""")
if seleccion == "1":

    a = int(input("Ingresar el valor incial a comparar\n→ "))
    b = int(input("Ingrese el valor sobre el cual se quiera comparar\n→ "))

    razon = mc.calcular_razon(a, b)
    indice = mc.calcular_indice(razon)
    proporcion = mc.calcular_proporcion()
    porcentaje = mc.calcular_porcentaje()

    print(f"La razon es → {razon}")
    print(f"El indice es → {indice}")
    print(f"La proporcion es → {proporcion}")
    print(f"El porcentaje es {porcentaje}")
    
elif seleccion == "2":
    
    ingreso = input("Ingrese la lista de los datos serparados por una coma\n→ ")
    lista = ingreso.split(',')
    lista = [int(numero) for numero in lista]

    #las listas valores para pruebas 
    #lista = [157,169,158,169,159,170,160,170,161,171,162,172,163,172,164,173,165,173,166,174,166,174,167,175,167,176,168,177,168,178,168,179]
    #lista = [14,14,15,15,15,16,16,16,16,17,17,18]
    if len(lista) > 20:
        print("\nSe ara la clasificacion de datos ")

        valores = df.calcular_valores(lista)
        intervalos = df.intervalos(valores)
        X = df.marca_clase(intervalos)
        f = df.frecuencia_intervalos(intervalos, lista)

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

    seleccion = input("¿Desea hacer los graficos? s / n\n→ ")
    if seleccion != "n":
        while True:
            seleccion = input("""
    ¿Qué grafico deseas hacer?

    1) Histograma
    2) Poligono de frecuencias
    3) Ojiva
    4) Ojiva porcentual
    5) Salir

    → """)
            if seleccion == "1":
                gf.Histograma(X, f)

            elif seleccion == "2":
                gf.Poligono_frecuencias(X, f)

            elif seleccion == "3":
                if len(lista) > 20:
                    intervalosm = intervalos  + [intervalos[-1]]
                    gf.Ojiva(intervalosm, F)
                else:
                    gf.Ojiva(X, F)

            elif seleccion == "4":

                if len(lista) > 20:
                    intervalosm = intervalos + [intervalos[-1]]

                    gf.Ojiva_porcentual(intervalosm, P)
                else:            
                    gf.Ojiva_porcentual(X, P)

            elif seleccion == "5":
                print("\nTerminaron las graficas")
                break
            
            else:
                print("Seleccion incorrecta")
    else:
        print("No se realizaron las graficas")

else:
    print("La seleccion feue incorrecata")