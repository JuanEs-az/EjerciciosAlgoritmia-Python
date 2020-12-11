#Ejercicio 10: Determinar si todos los numeros son iguales

#Construir un algoritmo que lea n numeros y determine si todos ellos son iguales
global _mensaje
_mensaje = "iguales"
n = int(input("Cuantos datos planea ingresar?\n"))
_datos = []
for each in range(1,n + 1):
    _datos.append(int(input("Dato " + str(each) + "\n")))
for i in range(0,len(_datos) - 1):
    if _datos[i] != _datos[i + 1]:
        _mensaje = "distintos"
        break
print("Los numeros insertados son " , _mensaje)
