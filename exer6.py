lista1 = [1, 2, 3, 4, 5, 6]

def separar_num(lista):
    pares = list(filter(lambda x: x % 2 == 0, lista))
    impares = list(filter(lambda x: x % 2 != 0, lista))
    return {'impares' : impares , 'pares' : pares}

print(separar_num(lista1))