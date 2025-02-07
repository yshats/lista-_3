lista = [1, -2, 0, 3, -5, 0]

def agrupar_num_categoria(numeros):
    positivos = list(filter(lambda x: x > 0, numeros))
    negativos = list(filter(lambda x: x < 0, numeros))
    zeros = list(filter(lambda x: x == 0, numeros))
    return {'positivos' : positivos, 'negativos' : negativos, 'zeros' : zeros}

print(agrupar_num_categoria(lista))