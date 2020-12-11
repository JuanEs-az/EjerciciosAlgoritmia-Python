#Ejercicio 29: Selección de elementos de un arreglo

#Construir un algoritmo que dado un arreglo de n elementos, encuentre e imprima el mayor y el menor de los
#valores almacenados

def MayorYMenor(elementos):
    mayor = elementos[0]
    menor = elementos[0]
    i = 0
    while i < len(elementos):
        if elementos[i] >= mayor:
            mayor = elementos[i]
        if i != 0:
            if elementos[i] <= menor:
                menor = elementos[i]
        i += 1
    return mayor,menor
arreglo = [2,2,4,5,6,2,8,2]
mayor,menor = MayorYMenor(arreglo)
print(f"{mayor} ES EL MAYOR\n{menor} ES EL MENOR")