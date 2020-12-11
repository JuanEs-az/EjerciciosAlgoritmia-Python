#Ejercicio 5: Determinar si un numero es divisor de otro

#Construir un algoritmo que dados dos numeros a y b, permita determinar si b es divisor entero de a

A = int(input("Ingrese el valor A\n"))
B = int(input("Ingrese el valor B\n"))
_modulo = A % B
if _modulo == 0:
    print(B , " es divisor entero de " , A)
else:
    print(B , " NO es divisor entero de " , A)