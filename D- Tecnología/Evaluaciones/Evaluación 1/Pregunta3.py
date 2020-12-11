#Escribir un programa que, usando un ciclo while, pida números enteros al usuario. El ciclo finaliza si se ingresa
#un cero. Al finalizar el ciclo, el programa debe imprimir la suma de todos los números ingresados y su promedio.
suma = 0
numerosIngresados = 0
while True:
    numero = int(input("Ingrese un numero entero: "))
    if numero == 0:
        break
    suma += numero
    numerosIngresados += 1
print(f"- LA SUMATORIA TOTAL DE LOS NUMEROS INGRESADOS FUE DE {suma}\n- LA CANTIDAD DE NUMEROS FUE DE {numerosIngresados}")
if numerosIngresados > 0:
    print(f"- EL PROMEDIO (SUMA/CANTIDAD) FUE {suma/numerosIngresados}")