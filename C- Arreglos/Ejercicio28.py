#Ejercicio 28: Primera ocurrencia de un elemento

#Construir un algoritmo que dado un arreglo de n numeros enteros (posiblemente repetidos), encuentre la primera
#posición en la cual se encuentra un elemento dado x dado del arreglo. de no encontrarse se deberá retornar -1

def PrimeraPosicion(x,elementos):
    for i,elemento in enumerate(elementos):
        if elemento == x:
            return i
    return -1
arreglo = [1,1,1,1,1,1,1,1,12,12,12,12,12,12,12,123,123,123,123,123]
print(PrimeraPosicion(int(input("Ingrese un numero\n")),arreglo))