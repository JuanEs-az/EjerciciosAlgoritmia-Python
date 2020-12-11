#Ejercicio 6: Determinar si un numero es par

#Construir un algoritmo que dado un numero determine si es par

A = int(input("Ingrese el valor A\n"))
_moduloPar = A % 2
if _moduloPar == 0:
    print(A , " es un numero par")
else:
    print(A , " es un numero impar")