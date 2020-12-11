#Ejercicio 7: Valor de la compra

#Construir un algoritmo que dado el valor de un artículo y la cantidad de artículos a comprar, determine el valor total a pagar deacuerdo 
#con las siguientes condiciones:

#Si se compran entre 5 y 10 artículos, se aplica un descuento del 10% sobre el total a pagar.

#Si se compran más de 10 artículos, se aplica un 20% sobre el total a pagar.

#En cualquier otro caso no se aplica descuento.#Ejercicio 7: Valor de la compra

#Construir un algoritmo que dado el valor de un artículo y la cantidad de artículos a comprar, determine el valor total a pagar deacuerdo 
#con las siguientes condiciones:

#Si se compran entre 5 y 10 artículos, se aplica un descuento del 10% sobre el total a pagar.

#Si se compran más de 10 artículos, se aplica un 20% sobre el total a pagar.

#En cualquier otro caso no se aplica descuento.#Ejercicio 7: Valor de la compra

#Construir un algoritmo que dado el valor de un artículo y la cantidad de artículos a comprar, determine el valor total a pagar deacuerdo 
#con las siguientes condiciones:

#Si se compran entre 5 y 10 artículos, se aplica un descuento del 10% sobre el total a pagar.

#Si se compran más de 10 artículos, se aplica un 20% sobre el total a pagar.

#En cualquier otro caso no se aplica descuento.

precio = float(input("Ingrese el precio total\n"))
cantidad = int(input("Ingrese la cantidad de artículos\n"))
_tenPercent = 10 / 100
_twentyPercent = 20 / 100
if cantidad >= 5 and cantidad < 10:
    precio -= precio * _tenPercent
elif cantidad > 10:
    precio -= precio * _twentyPercent
print(precio)
