"""
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra
que contiene y su frecuencia. (HECHO)

Escribir otra función que reciba el diccionario generado con la función
anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
"""

def Frecuencia(String):
    Lista = String.lower().split(" ")
    Dict = {}
    for palabra in Lista:
        if palabra in Dict:
            print("continuo")
            continue
        Dict[palabra] = Lista.count(palabra)
    return Dict

def MayorFrecuencia(Dict):
    keys = list(Dict.keys())
    items = list(Dict.values())
    frecuencia = max(items)
    palabra = keys[items.index(frecuencia)]
    return (palabra,frecuencia)

