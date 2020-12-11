#Ejercicio 13: Sucesion de Fibonacci

#Construir un algoritmo que presente los primeros 20 numeros de la sucesión de Fibonacci

A = 1
B = 1
i = 1
while i <= 20:
    print(A)
    C= A + B
    B = A
    A = C
    i+=1
