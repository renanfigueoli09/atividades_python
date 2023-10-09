import pandas as pd
import re

dados = pd.read_csv('imdb-reviews-pt-br.csv')

def limpar_lista(lista_palavras):
    indice = 0
    regex = r"[!\"#\$%&\'\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`{\|}~]"
    s = ""
    lista = []

    for i in lista_palavras:
        if i.find("\n") > 0:
            l2 = i.split("\n")
            l2_limpa = limpar_lista(l2)
            lista.extend(l2_limpa)
        elif i != "":
            palavra_limpa = i.lower()
            palavra_limpa = re.sub(regex, s, palavra_limpa, 0, re.MULTILINE)
            lista.append(palavra_limpa)
        indice += 1

    return lista

dados['text_pt_limpo'] = dados['text_pt'].str.split().apply(limpar_lista).str.join(' ')

print(dados[['text_pt', 'text_pt_limpo']].head())
