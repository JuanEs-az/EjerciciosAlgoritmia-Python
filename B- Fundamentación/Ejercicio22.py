#Ejercicio 22: Estudiantes que aprueban la asignatura

#Construir un algoritmo que lea los datos de codigo y tres notas parciales (n1, n2 y n3) de un conjunto de estudiantes.
#para cada estudiante se deberá calcular e imprimir su nota definitiva, teniendo en cuenta que la primera nota parcial 
#aporta el 35 porciento a la nota definitiva, la segunda nota aporta el 35 porciento  y la ultima nota aporta el 30 porciento
#restante.

#No se conoce por anticipado el numero de estudiantes, por lo cual el algoritmo deberá continuar solicitando datos de estudiantes
#hasta que se especifique cero como codigo de estudiante.

#Tambien se deberá imprimir el numero de estudiantes que aprueban la asignatura, es decir, que su nota definitiva sea mayor que 3,0.

#Ademas se deberá validar que los datos ingresados para las notas parciales de cada estudiante se encuentra en el rango de 0,0 y 5,0.

class Estudiante:
    def __init__(self,codigo,nota1,nota2,nota3,porcentajesR):
        self.codigo = codigo
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.notaValida = (self.nota1 >= 0.0 and self.nota1 <= 5.0) and (self.nota2 >= 0.0 and self.nota2 <= 5.0) and (self.nota3 >= 0.0 and self.nota3 <= 5.0)
        self.notaDef = self.nota1 * (porcentajesR[0] / 100) + self.nota2 * (porcentajesR[1] / 100) + self.nota3 * (porcentajesR[2] / 100)
        self.aprueba = self.notaDef >= 3.0
    def __len__(self):
        if self.aprueba:
            return 1
        elif not self.aprueba:
            return 0
    def __str__(self):
        return f"{self.codigo}\t\t{self.notaDef}"
estudiantes = []
aprobaron = 0
contadorAlumnos = 0
while True:
    codigo = input("Ingrese codigo del estudiante\n")
    if codigo == "0":
        break
    nota1 = float(input(f"ingrese la nota 1 del estudiante {codigo}\n"))
    nota2 = float(input(f"ingrese la nota 2 del estudiante {codigo}\n"))
    nota3 = float(input(f"ingrese la nota 3 del estudiante {codigo}\n"))
    if nota1 > 5 or nota2 > 5 or nota3 > 5:
        print("Nota no valida")
        continue
    estudiantes.append(Estudiante(codigo,nota1,nota2,nota3,(35,35,30)))
print("CODIGO\t\tNOTA DEFINITIVA")
for estudiante in estudiantes:
    if estudiante.aprueba:
        print(str(estudiante))
    aprobaron += len(estudiante)
print("APROBARON\t\t",aprobaron)
