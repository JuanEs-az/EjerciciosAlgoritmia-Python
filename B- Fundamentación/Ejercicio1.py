#Ejercicio 1: Intercambio de valores

#Construir un algoritmo que lea dos numeros enteros de dos variables, intercambie sus valores almacenados en ellas
#y luego imprima los valores resultantes.

A = int(input("Ingrese el Valor A\n"))
B = int(input("Ingresee el Valor B\n"))
_auxiliar = A 
A = B
B = _auxiliar
print("A = " , A)
print("B = " , B)