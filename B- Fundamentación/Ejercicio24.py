#Ejercicio 24: Estudiantes con alguna nota menor al promedio

#Construir un algoritmo que dados el codigo y tres notas parciales con porcentajes de 30%, 30% y 40%, respectivamente
#de un numero indeterminado de estudiantes , imprima el codigo, las notas parciales y la nota definitiva de aquellos
#que posean alguna calificación menor que el promedio de las notas finales de todo el curso.

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
        return f"---\t{self.codigo}\t---\nNOTA 1 :{self.nota1}\nNOTA 2: {self.nota2}\nNOTA 3: {self.nota3}\nDEFINITIVA: {self.notaDef}"
info = (30,30,40)
codigoEstudiante = None
estudiantes = []
promedio = {
    "nota1" : 0,
    "nota2" : 0,
    "nota3" : 0,
    "definitiva" : 0
    }
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
    promedio["nota1"] += nota1
    promedio["nota2"] += nota2
    promedio["nota3"] += nota3
    promedio["definitiva"] += alumno.notaDef
promedio["nota1"] /= len(estudiantes)
promedio["nota2"] /= len(estudiantes)
promedio["nota3"] /= len(estudiantes)
promedio["definitiva"] /= len(estudiantes)
print("ESTUDIANTES CON NOTAS MENORES AL PROMEDIO")
for estudiante in estudiantes:
    if estudiante.nota1 < promedio["nota1"] or estudiante.nota2 < promedio["nota2"] or estudiante.nota3 < promedio["nota3"] or estudiante.notaDef < promedio["definitiva"]:
        print(str(estudiante))
print(
f"""
EL PROMEDIO DE LAS NOTAS FUÉ:
NOTA 1                  {promedio["nota1"]}
NOTA 2                  {promedio["nota2"]}
NOTA 3                  {promedio["nota3"]}
DEFINITIVA              {promedio["definitiva"]}
"""
)