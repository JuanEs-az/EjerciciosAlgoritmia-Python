#Ejercicio 11: Verificar si todos los numeros son pares

#Construir un codigo que dados n numeros, determine si todos ellos son pares o no

global _mensaje
n = int(input("Cuantos datos planea ingresar?\n"))
_datos = []
for each in range(1,n + 1):
    _datos.append(int(input("Dato " + str(each) + "\n")))
for i in range(0,len(_datos) - 1):
    _modulo = _datos[i] % 2
    if _modulo > 0:
        _mensaje = "No Todos los numeros son pares"
        break
    else:
        _mensaje = "Todos los nuemros son pares"
print(_mensaje)

