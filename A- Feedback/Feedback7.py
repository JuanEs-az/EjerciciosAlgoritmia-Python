def retornoCuadrados(lista):
    retorno = []
    for numero in lista:
        if isinstance(numero,(int,float)):
            retorno.append(numero ** 2)
        else:
            retorno.append("NaN")
    return retorno
