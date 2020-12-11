#Ejercicio 18: Factorial de un numero

#Construir un algoritmo que dado un numero entero mayor o igual que cero, calcule e imprima su factorial

global n
n = int(input("Ingrese su numero\n"))
def Factorial(numero = n):
    if numero == 1 or numero == 0:
       return 1
    else:
        return numero * Factorial(numero - 1)
print("el factorial de {} es {}".format(n,Factorial()))