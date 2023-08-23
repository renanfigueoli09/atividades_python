import nltk
from nltk.corpus import stopwords

texto = """rato roeu a roupa do rei de Roma,

O rato roeu a roupa do rei da Rússia,

O rato roeu a roupa do RodovaIho...

O rato a roer roía

E a rosa Rita Ramalho do rato a roer se ria.

O rato roeu a roupa do rei de roma

a rainha com raiva roeu o resto."""

texto = texto.lower()
characters = ".,\n"
for x in range(len(characters)):
    texto = texto.replace(characters[x],"")
tokens = texto.split()

v_token = list(set(tokens))

nltk.download('stopwords')
p = set(stopwords.words('portuguese'))

v = [palavra for palavra in v_token if palavra not in p]

print("vocabulário:")
print(v)
