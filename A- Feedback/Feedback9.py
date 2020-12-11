"""
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno,
tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función
a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado
de aplicar la función a esos enteros.
"""
from math import sin,cos,tan,log,e,radians,degrees,exp
def Calculadora(op,dato1):
    if op == "sin":
        return f"sin({dato1}) = {degrees(sin(radians(dato1)))}"
    elif op == "cos":
        return f"cos({dato1}) = {degrees(cos(radians(dato1)))}"
    elif op == "tan":
        return f"tan({dato1}) = {degrees(tan(radians(dato1)))}"
    elif op == "ln":
        return f"ln({dato1}) = {log(dato1,e)}"
    elif op == "exp":
        return f"exp({dato1}) = {exp(dato1)}"
opPosibles = ["sin","ln","cos","tan","exp"]
op = input("Que operacion desea realizar?\n")
numero = int(input("Hasta que numero desea realizarla?\n"))
if op.lower() in opPosibles:
    for i in range(1,numero + 1):
        print(Calculadora(op,i))
else:
    print("Operacion no disponible")