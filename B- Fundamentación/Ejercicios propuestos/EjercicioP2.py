#Ejercicio 2:
#Construir un algoritmo que dados n numeros, encuentre el mayor y el menor de ellos.

def isSortedNumericly(List):
    retorno = True
    for i,el in enumerate(List):
        if i < len(List) - 1:
            if List[i] > List[i + 1]:
                retorno = False
                break
    return retorno

def SortNumeric(List):
    for i,el in enumerate(List):
        if i < len(List) - 1:
            if List[i] >= List[i + 1]:
                 List[i],List[i + 1] = List[i + 1] ,List[i]
    if isSortedNumericly(List):
        return List
    else:
        return SortNumeric(List)

n = int(input("Cuantos datos tienes?"))
numeros = []
for numero in range(1, n + 1):
    numeros.append(float(input(f"DATO {numero}:\n")))
sortedNumeros = SortNumeric(numeros)
print(f"EL NUMERO MAYOR ES {sortedNumeros[len(sortedNumeros) - 1]}")    
print(f"EL NUMERO MENOR ES {sortedNumeros[0]}")   

