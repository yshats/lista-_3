def nomes_com_mais_de_cinco_letras(nomes):
    return list(filter(lambda nome: len(nome) >= 5, nomes))

lista = ["Ana", "Lucas", "Fernanda", "João"]
print(nomes_com_mais_de_cinco_letras(lista))