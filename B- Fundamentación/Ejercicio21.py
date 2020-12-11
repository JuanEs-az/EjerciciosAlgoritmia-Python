#Ejercicio 21: Maximo Común Divisor

#Construir un algoritmo que dados dos numeros enteros positivos A y B halle e imprima su maximo común divisor

numeros = [int(input("Ingrese el valor A\n")) , int(input("Ingrese el valor B\n"))]
divisoresNumeros = []
primos = []
cuenta = 999
cuentaAtras = cuenta
divisoresPorNumero = []
global mcd
mcd = 1
#Factores Primos
while cuenta > 1:
    while cuentaAtras >= 1:
        modulo = cuenta % cuentaAtras
        if modulo == 0:
            divisoresPorNumero.append(cuentaAtras)
        cuentaAtras -= 1
    if len(divisoresPorNumero) <= 2:
        primos.append(cuenta)
    divisoresPorNumero = []
    cuenta -= 1
    cuentaAtras = cuenta
primos.reverse()
cuenta = 0
#Extraccion de los divisores de los numeros
for numero in numeros:
    while numero > 1:
        modulo = numero % primos[cuenta]
        if modulo == 0:
            divisoresPorNumero.append(primos[cuenta])
            numero /= primos[cuenta]
        else:
            cuenta += 1
    divisoresNumeros.append(divisoresPorNumero)
    divisoresPorNumero = []
    cuenta = 0
for divisores in divisoresNumeros:
    divisores.insert(0,1)
#Optimizar
XdivisoresNumeros = divisoresNumeros
x0 = XdivisoresNumeros[0].pop()
x1 = XdivisoresNumeros[1].pop()
if x0 >= x1:
    mayorFactorFinal = x0
else:
    mayorFactorFinal = x1
del(cuentaAtras,divisoresPorNumero,XdivisoresNumeros,x0,x1)
#Extracción del MCD de los numeros
for primo in primos:
    if divisoresNumeros[0].count(primo) == 0 or divisoresNumeros[1].count(primo) == 0:
        continue
    if divisoresNumeros[0].count(primo) > divisoresNumeros[1].count(primo):
        menorCantidadDelPrimo = divisoresNumeros[1].count(primo)
    else:
        menorCantidadDelPrimo = divisoresNumeros[0].count(primo)
    cuenta = 0
    while cuenta < menorCantidadDelPrimo:
        mcd *= primo
        cuenta += 1
    if primo == mayorFactorFinal:
        break
    cuenta = 0
print(mcd)

        

    
        
    



    
