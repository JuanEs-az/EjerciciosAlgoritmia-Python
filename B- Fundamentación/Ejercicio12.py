#Ejercicio 12: Determinar si un numero es primo

#Construir un algoritmo que dado un numero n, determine si es primo o no.

global _mensaje
_mensaje = "Tu numero es primo"
n = int(input("Ingrese el valor de su numero\n"))
_auxiliar = n
_auxiliar-=1
while _auxiliar > 1:
    _modulo = n % _auxiliar
    if _modulo == 0:
        _mensaje = "Tu numero NO es primo"
        break
    _auxiliar-=1
print(_mensaje)

