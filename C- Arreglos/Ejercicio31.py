#Ejercicio 31: El par de puntos mas cercanos

#Construir un algoritmo que dado un arreglo de n puntos, encuentre e imprima el par de puntos mas cercanos entre
#sí y la distancia que existe entre ellos. Para cada punto se proporcionan coordenadas (x,y). La distancia entre
#estos puntos se calcula usando la formula de Euclides

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self,otro):
        return (((self.x - otro.x) ** 2) + ((self.y - otro.y) ** 2)) ** .5
    def __str__(self):
        return str((self.x,self.y))
def Menor(elementos):
    menor = elementos[0]
    i = 0
    indiceMenor = 0
    while i < len(elementos):
        if i != 0:
            if elementos[i] <= menor:
                menor = elementos[i]
                indiceMenor = i
        i += 1
    return {'value' : menor , 'index' : indiceMenor}
puntos = [Punto(1,1),Punto(2,2),Punto(4,4),Punto(5,1),Punto(10,1),Punto(1,10),Punto(2,1)]
distanciasMenores = {
    'values' : [],
    'points' : []
}
i = 0
while i < len(puntos) - 1:
    distancias = []
    puntosDescarte = []
    j = i + 1
    while j < len(puntos):
        puntosDescarte.append((puntos[i],puntos[j]))
        distancias.append(puntos[i] * puntos[j])
        j += 1
    distanciaMenor = Menor(distancias)
    distanciasMenores['values'].append(distanciaMenor['value'])
    distanciasMenores['points'].append(puntosDescarte[distanciaMenor['index']])
    i += 1
distanciaMenor = Menor(distanciasMenores['values'])
valor = distanciaMenor['value']
puntos = distanciasMenores['points'][distanciaMenor['index']]
print(
f"""
                DISTANCIA MENOR
PUNTO 1  {puntos[0]}
PUNTO 2  {puntos[1]}
DISTANCIA  {valor}
""")