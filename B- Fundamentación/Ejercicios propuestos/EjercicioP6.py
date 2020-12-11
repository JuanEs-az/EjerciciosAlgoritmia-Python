#Ejercicio 6:
#Construir un algoritmo que dados n puntos, encuentre el mas cercano y el mas lejano al origen
puntos = []
distancias = []

X = float(input("Ingrese el valor de X:  "))
Y = float(input("Ingrese el valor de Y:  "))
puntos.append((X,Y))
distancias.append(((X ** 2) + (Y ** 2))**.5)
while True:
    X = float(input("Ingrese el valor de X:  "))
    Y = float(input("Ingrese el valor de Y:  "))
    if X == 0 and Y == 0:
        break
    puntos.append((X,Y))
    distancias.append(((X ** 2) + (Y ** 2))**.5)

menor = puntos[distancias.index(min(distancias))]
mayor = puntos[distancias.index(max(distancias))]
print(
f"""
\t\t\t\t+ CERCANO --> {menor}
\t\t\t\t+ LEJANO --> {mayor}
""")