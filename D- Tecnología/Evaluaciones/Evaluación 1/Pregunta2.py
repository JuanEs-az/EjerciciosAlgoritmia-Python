while True:
    x = input("Ingresa un numero o * para terminar")
    if x == "*":
        break
    elif int(x) == 0:
        print("El numero es cero")
    elif int(x) > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")

