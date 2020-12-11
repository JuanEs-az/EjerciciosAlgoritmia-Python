#Ejercicio 32: Inserción de elementos al final de un arreglo

#Construir una función que permita insertar un nuevo elemento al final de un arreglo de numeros enteros. 
#La función deberá retornar la cantidad de elementos totales almacenados. Suponga que el arreglo puede
#crecer automaricamente

def InsertarElemento(elementos, elemento):
    i = 0
    elementosRetorno = []
    while i < len(elementos):
        elementosRetorno += [elementos[i],]
        i += 1
    elementosRetorno  += [elemento,]
    return elementosRetorno

arreglo = [1,2,3,4,5,6,7]
arreglo = InsertarElemento(arreglo,8)
print(arreglo)
