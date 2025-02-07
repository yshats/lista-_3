from functools import reduce

def calcular_media_ponderada(alunos):
    resultado = {}
    for aluno, valores in alunos.items():
        peso = valores[-1]
        notas = valores[:-1]
        soma_ponderada = reduce(lambda acc, nota: acc + (nota * peso), notas, 0)
        media = soma_ponderada / (peso * len(notas))
        resultado[aluno] = media
    return resultado


dados = {
    "João": [8, 7, 9, 2],  # notas: 8, 7, 9; peso: 2
    "Ana": [5, 6, 7, 3]    # notas: 5, 6, 7; peso: 3
}

print(calcular_media_ponderada(dados))