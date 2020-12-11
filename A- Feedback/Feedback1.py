"""
Feedback 1: 
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al
usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""

Inicial = input("Dime tu nombre\n")[0].upper()
sexo = input("A que genero perteneces (M/H)\n")[0].upper()
if (sexo == "M" and Inicial <= "M") or (sexo == "H" and Inicial >= "N"):
    grupo = "A"
else:
    grupo = "B"
print("PERTENECES AL GRUPO",grupo)
