#Ejercicio 19: Calculo de la potencia entera positiva

#Construir un algoritmo que dados un numero real x y un numero entero y >= 0, calcule el valor de la potencia x a la y

A = int(input("Inserte la Base A\n"))
_aux = A
n = int(input("Ingrese el Exponente n\n"))
n -= 2
_i = 0
while _i <= n:
    A *= _aux
    _i += 1
print(A)
