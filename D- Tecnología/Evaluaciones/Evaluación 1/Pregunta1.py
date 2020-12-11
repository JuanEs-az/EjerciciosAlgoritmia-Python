x = input("Ingresa un numero o * para terminar")
cantidadDePositivos = 0
while x != "*":
    if int(x) == 0:
        print("El numero es cero")
    elif int(x) > 0:
        print("El numero es positivo")
        cantidadDePositivos += 1
    else:
        print("El numero es negativo")
    x = input("Ingresa un numero o * para terminar")
print(f"Se ingresaron {cantidadDePositivos} numeros positivos")
