#Ejercicio 20: Calculo de Pi

#Desarrollar un algoritmo que permita calcular el valor de pi mediante el calculo de la formula de Leibniz
#El algoritmo deberá solicitar un numero k < 0, que representará el termino hasta el cual se deberá realizar el calculo 

k = int(input("Ingrese su numero\n"))
_pi = 0
for each in range(0,k + 1):
    num = 1
    _mod = each % 2
    if _mod != 0:
        num = -1
    _pi += num /(2 * each + 1)
_pi *= 4
print(_pi)


    
    
