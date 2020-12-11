#Ejercicio 30: Promedio de datos de un arreglo

#Construir un algoritmo que dado  un arreglo de n numeros que calcule su promedio
def CalcularPromedio(elementos):
    cantidad = len(elementos)
    suma = 0
    for elemento in elementos:
        if not isinstance(elemento,(int,float)):
            cantidad -= 1
            continue
        suma += elemento
    return suma/cantidad
arreglo = list(range(1,100))
print(f"El promedio de los elementos del arreglo es {CalcularPromedio(arreglo)}")