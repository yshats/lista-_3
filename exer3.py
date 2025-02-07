from functools  import reduce
lista = [1, 2, 3, 4]
soma_total = reduce(lambda x, y: x + y, lista)
print(soma_total)