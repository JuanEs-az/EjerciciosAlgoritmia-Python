"""
Feedback 2:
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	            Tipo impositivo
Menos de 10000€	        5%
Entre 10000€ y 20000€	15%
Entre 200000€ y 35000€	20%
Entre 350000€ y 60000€	30%
Más de 60000€	        45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""

rentaAnual = float(input("Cuanto pagas anualmente de renta?\n"))
if rentaAnual < 10000:
    pImpuesto = 5
elif rentaAnual >= 10000 and rentaAnual < 20000:
    pImpuesto = 15
elif rentaAnual >= 20000 and rentaAnual < 35000:
    pImpuesto = 20
elif rentaAnual >= 35000 and rentaAnual < 60000:
    pImpuesto = 30
else:
    pImpuesto = 45
Impuesto = rentaAnual * (pImpuesto/100)
print(
f"""
RENTA ANUAL         {rentaAnual}€
PORCENTAJE IMP      {pImpuesto}%
IMPUESO             {Impuesto}€
"""
)