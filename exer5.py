def elevar_num_quadrado_ordenalos(numeros):
    return list(map(lambda numero: numero ** 2, numeros))

lista = [3, 1, 4, 2]

print(sorted(elevar_num_quadrado_ordenalos(lista)))