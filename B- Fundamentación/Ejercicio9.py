#Ejercicio 9: Sumatoria de n primeros numeros naturales

#Construir un algoritmo que dado un numero natural n, calcule la sumatoria de los numeros naturales del 1 al n

n = int(input("Establezca un limite\n"))
_sumatoria = 0
for each in range(1,n + 1):
    _sumatoria += each
print("La sumatoria de los numeros entre 1 y " , n , " es igual a " , _sumatoria )