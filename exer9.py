entrada = [(2, 8), (4, 5, 6), (1, 2)]

def media_tupla(tuplas):
    media = map(lambda t: (t, sum(t)/len(t)), tuplas)
    filtro = filter(lambda item: item[1] >= 5, media)
    return list(map(lambda item: item[0], filtro))

print(media_tupla(entrada))