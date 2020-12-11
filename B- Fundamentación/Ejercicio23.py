#Ejercicio 37: Estudiantes con nota menor que el promedio

#Construir un algoritmo que dados el codigo y tres notas parciales con porcentajes 30%, 30% y 40%, respectivamente
#de un numero indeterminado de estudiantes, imprima el codigo y la nota definitiva sí esta es menor que el promedio
#de las definitivas de todo el curso.

#El algoritmo deberá continuar solicitando datos hasta que se especifique 0 como codigo de estudiante.
from math import fsum
class Estudiante:
    def __init__(self,codigo,nota1,nota2,nota3,info):
        self.codigo = codigo
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.notaValida = (self.nota1 >= 0.0 and self.nota1 <= 5.0) and (self.nota2 >= 0.0 and self.nota2 <= 5.0) and (self.nota3 >= 0.0 and self.nota3 <= 5.0)
        self.notaDef = self.nota1 * (info[0] / 100) + self.nota2 * (info[1] / 100) + self.nota3 * (info[2] / 100)
        self.aprueba = self.notaDef >= 3.0
    def __str__(self):
        return f"{self.codigo}\t\t{self.notaDef}"
info = (30,30,40)
codigoEstudiante = None
estudiantes = []
promedio = 0
while True:
    codigoEstudiante = input("Ingrese el codigo del estudiante\n")
    if codigoEstudiante == "0":
        if len(estudiantes) == 0:
            exit()
        break
    nota1 = float(input("Ingrese la nota 1 del estudiante\n"))
    nota2 = float(input("Ingrese la nota 2 del estudiante\n"))
    nota3 = float(input("Ingrese la nota 3 del estudiante\n"))
    if nota1 > 5 or nota2 > 5 or nota3 > 5:
        print("Nota no valida")
        continue
    alumno = Estudiante(codigoEstudiante,nota1,nota2,nota3,info)
    estudiantes.append(alumno)
    promedio += alumno.notaDef
promedio/= len(estudiantes)
print("\t\tAPROBARON")
for estudiante in estudiantes:
    if estudiante.notaDef >= promedio:
        print(str(estudiante))
print("\t\tREPROBARON")
for estudiante in estudiantes:
    if estudiante.notaDef <= promedio:
        print(str(estudiante))
print("EL PROMEDIO DE NOTAS FUÉ",promedio)
