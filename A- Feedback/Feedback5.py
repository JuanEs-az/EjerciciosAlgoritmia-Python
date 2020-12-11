"""
Feedback 5:
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números
impares desde 1 hasta ese número separados por comas.
"""
numero = int(input("Dame un numero entero positivo, es una orden\n"))
for number in range(1,numero + 1):
    if number % 2 == 1:
        print(number)
