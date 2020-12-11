#Ejercicio 33. Insertar al final de un arreglo de tamaño limitado

#Construir una función que permita insertar un nuevo elemento al final de un arreglo de numeros enteros. 
#La función deberá retornar la cantidad de elementos totales almacenados.Suponga que el arreglo solo puede crecer
#hasta un limite m dado. En caso de tratar de insertar un elemento más allá de la capacidad del arreglo 
#se deberá retornar -1.
arreglo = [1,2,3]
m = int(input("Ingrese el limite de elementos: "))
def añadirElementoAlFinal(nuevoElemento):
    global arreglo
    arreglo += [nuevoElemento,]
    return len(arreglo) if len(arreglo) < m else -1
while añadirElementoAlFinal(int(input("Ingresa un nuevo elemento: "))) != -1:
    pass
print("Ups... Alcanzaste el limite")
print(arreglo)