#Ejercicio 16: Solo los mayores de edad

#Construir un algoritmo que dados la edad y el nombre de n personas, imprima por pantalla solo el nombre y la edad de las personas mayores
#de edad. Se considera que una persona es mayor de edad si tiene 18 años o más.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def Mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
_Grupo = []
n = int(input("Ingrese el Numero de Personas en su grupo\n"))
for counter in range(0 , n - 1):
    Nombre=input("Ingrese el Nombre de la Persona\n")
    Edad=int(input("ingrese la edad de la persona\n"))
    _Grupo.append(Persona(Nombre,Edad))
for each in _Grupo:
    if each.Mayor_de_edad():
        print(each.nombre," ",each.edad)
