#Ejercicio 17: Suma de Pares

#Construir un algoritmo que dados n numeros, calcule e imprima la suma de los numeros pares

n = int(input("Ingrese el numero de dato\n"))
_pares = []
_suma = 0
for each in range(1 , n + 1):
    numero = float(input("Ingrese el Dato"+str(each)+"\n"))
    _modulo = numero % 2
    if _modulo == 0:
        _suma+=numero
#for each in _pares:
#    _suma+=each
print(_suma)
    