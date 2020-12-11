#Ejercicio 27: Buscar elementos de un arreglo

#Construir un algoritmo que dado un arreglo de n numeros enteros (posiblemente repetidos), determine si un 
#elemento x se encuentra almacendo en un arreglo

def SoloNumeros(elementos):
    for elemento in elementos:
        if not isinstance(elemento,(int,float)):
            return False
    return True
def Existe(x,elementos):

    for elemento in elementos:
        if elemento == x:
            return True
    return False
arreglo = [1,3,5,7,9,11,13,17,19,23]
if SoloNumeros(arreglo):
    if Existe(float(input("Ingrese un numero\n")),arreglo):
        print("El elemento ingresado está dentro del arreglo")
    else:
        print("El elemento ingresado NO está dentro del arreglo")
else:
    print("El arreglo no contiene solo numeros\nno podemos gestionar lo que hay en su interior")
