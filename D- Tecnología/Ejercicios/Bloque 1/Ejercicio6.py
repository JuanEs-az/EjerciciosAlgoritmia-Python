numeroIngresado = int(input("Ingrese un numero: "))
contador = 1
while contador <= numeroIngresado:
    if numeroIngresado % contador == 0:
        print(contador)
    contador += 1