#Ejercicio 14: Promedio de n numeros

#Construir un algoritmo que dada una serie de numeros, calcule su promedio. Suponga que los numeros son enteros y positivos. El algoritmo
#deberá terminar cuando el numero leído sea menor o igual que cero

global datos
datos = []
_i = 0
_suma = 0
while True:
    datos.append(int(input("Dato {}\n".format(_i))))
    if datos[_i] <= 0:
        datos.pop()
        break
    _i+=1
for each in datos:
    _suma+=each
_promedio = _suma / len(datos)
print("El promedio es: {}".format(_promedio))