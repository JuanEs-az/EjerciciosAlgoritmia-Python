#Ejercicio 25: Inicializar un arreglo unidimensional

#Contruir un algoritmo que inicialice e imprima un arreglo de n elementos que deberá almacenar en cada posición
#en el indice correspondiente. El numero n es proporcionado por el usuario.

list = []
for _ in range(1,int(input("Cuantos numero quieres recoger?\n"))):
    list.append(int(input("Ingrese un elemento:\n")))
print(list)