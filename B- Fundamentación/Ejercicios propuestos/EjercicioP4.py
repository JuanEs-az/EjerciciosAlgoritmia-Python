#Ejercicio 4:
#Construir un algoritmo que dadas dos fechas (año, mes, y día), calcule e imprima el numero de horas
#minutos y segundos transcurridos entre ellas. Tenga en cuenta que las fechas no se ingresan de forma ordenada
#es decir que la primera fecha ingresada puede ser menor, igual, o mayor a la segunda.

fecha1 = {
    "AÑO" : int(input("Ingrese el año de la primera fecha\n")),
    "MES" : int(input("Ingrese el mes de la primera fecha\n")),
    "DIA" : int(input("Ingrese el día de la primera fecha\n"))
}
fecha2 = {
    "AÑO" : int(input("Ingrese el año de la segunda fecha\n")),
    "MES" : int(input("Ingrese el mes de la segunda fecha\n")),
    "DIA" : int(input("Ingrese el día de la segunda fecha\n"))
}
if fecha1["AÑO"] > fecha2["AÑO"]:
    fechaMayor = fecha1
elif fecha2["AÑO"] > fecha1["AÑO"]:
    fechaMayor = fecha2
else:
    if fecha1["MES"] > fecha2["MES"]:
        fechaMayor = fecha1
    elif fecha2["MES"] > fecha1["MES"]:
        fechaMayor = fecha2
    else:
        if fecha1["DIA"] > fecha2["DIA"]:
            fechaMayor = fecha1
        elif fecha2["DIA"] > fecha1["DIA"]:
            fechaMayor = fecha2
        else: 
            print("Las fechas son iguales")
            exit()


if fecha1 == fechaMayor:
    fechaMenor = fecha2
else:
    fechaMenor = fecha1

difDias = fechaMayor["DIA"] - fechaMenor["DIA"] 
difMes = fechaMayor["MES"] - fechaMenor["MES"]
difAno = fechaMayor["AÑO"] - fechaMenor["AÑO"]
diferenciaTotal = difDias + (difMes * 30) + (difAno * 360)
totalEnMedidas = {
    "DIAS" : diferenciaTotal,
    "HORAS" : diferenciaTotal * 24,
    "MINUTOS" : diferenciaTotal * 24 * 60,
    "SEGUNDOS" : diferenciaTotal * 24 * 60 * 60
}

print(
f"""
\t\t\t{fecha1["DIA"]}/{fecha1["MES"]}/{fecha1["AÑO"]}  &  {fecha2["DIA"]}/{fecha2["MES"]}/{fecha2["AÑO"]} 
\t\t\t{totalEnMedidas["DIAS"]} dias
\t\t\t{totalEnMedidas["HORAS"]} horas
\t\t\t{totalEnMedidas["MINUTOS"]} minutos
\t\t\t{totalEnMedidas["SEGUNDOS"]} segundos
""")