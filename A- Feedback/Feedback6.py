"""
Feedback 6:
Diseñar un algoritmo que recree las funciones del .upper y .lower. y que le pr
egunte al usuario una palabra y le dé la opción de convertir su texto a 
mayúscula o minuscula SIN usar la función upper o lower
"""
texto = input("Mucho tepsto\n")
opciones = input("Todo 'mayuscula' o 'minuscula'?\n")
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if opciones == "mayuscula":
    for letra in texto:
        if not(letra in upper):
            index = lower.index(letra)
            print(upper[index],end = "")
        else:
            print(letra,end="")
else:
    for letra in texto:
        if not(letra in lower):
            index = upper.index(letra)
            print(lower[index],end = "")
        else:
            print(letra,end="")


    
