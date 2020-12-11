#Ejericio 3:
#Construir un algoritmo en el cual dados tres datos que representan una hora (hora, minuto, segundo)
#en formato de 24 horas, exprese la misma en formato de doce horas (a.m - p.m).
hora = int(input("HORAS\n"))
minuto = int(input("MINUTOS\n"))
segundo = int(input("SEGUNDOS\n"))
formato = "a.m"
if hora > 12:
    hora -= 12
    formato = "p.m"
elif hora == 12:
    formato = "m"
elif hora == 0:
    hora = 12
    formato = "p.m"
else:
    formato = "a.m"

print(f"{hora}:{minuto}:{segundo} {formato}")
