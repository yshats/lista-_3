from functools import reduce

lista = ["casa", "python", "lambda"]

def contar_letras(letras):
    contar = map(lambda letra: len(letra), letras)
    soma = reduce(lambda x,y: x + y, contar)
    return soma

print(contar_letras(lista))