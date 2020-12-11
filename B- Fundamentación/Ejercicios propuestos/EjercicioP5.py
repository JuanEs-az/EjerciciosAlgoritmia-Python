#Ejercicio 5:
#Construir un algoritmo que dados tres puntos, encuentre el par de ellos cuya distancia euclidiana es menor.
puntoA = (float(input("Xa : ")) , float(input("Ya : ")) )
puntoB = (float(input("Xb : ")) , float(input("Yb : ")) )
puntoC = (float(input("Xc : ")) , float(input("Yc : ")) )
distancias = {
    "A & B" : (((puntoA[0] - puntoB[0]) ** 2)  +  ((puntoA[1] - puntoB[1]) ** 2)) ** .5, 
    "B & C" : (((puntoB[0] - puntoC[0]) ** 2)  +  ((puntoB[1] - puntoC[1]) ** 2)) ** .5, 
    "A & C" : (((puntoA[0] - puntoC[0]) ** 2)  +  ((puntoA[1] - puntoC[1]) ** 2)) ** .5, 
}
for distancia in distancias:
    print(f"{distancia} -- {distancias[distancia]}")
print(f"{min(distancias.values())}")