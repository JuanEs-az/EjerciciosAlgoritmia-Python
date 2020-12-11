#Ejercicio 26: Inicializar un arreglo bidimensional

#Desarrollar un algoritmo que permita inicializar una matriz de n * n elementos, dispuestos como se muestra
#en la tabla 15 para n = 5.

n = int(input("Establezca un limite"))
list = []
for _ in range(1,n+1):
    microList = []
    for _ in range(1,n+1):
        microList.append(int(input("Ingresa un dato: ")))
    list.append(microList)
print("[")
for microList in list:
    print("    ",microList,end = ", \n")
print("]")