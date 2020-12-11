#Ejercicio 1:
#Construir un algoritmo que dados tres numeros, encuentre el mayor y el menor de ellos.
nA = int(input("Ingrese el valor de A"))
nB = int(input("Ingrese el valor de B"))
nC = int(input("Ingrese el valor de C"))
if nA > nB and nA > nC:
    mayor = nA
    if nB > nC:
        menor = nC
    else:
        menor = nB
elif nB > nA and nB > nC:
    mayor = nB
    if nA > nC:
        menor = nC
    else:
        menor = nA
elif nC > nA and nC > nB:
    mayor = nC
    if nB > nA:
        menor = nA
    else:
        menor = nB
else:
    print("Todos son iguales")
    exit()
print("El mayor es",mayor)
print("El menor es",menor)