texto = """rato roeu a roupa do rei de Roma,

O rato roeu a roupa do rei da Rússia,

O rato roeu a roupa do RodovaIho...

O rato a roer roía

E a rosa Rita Ramalho do rato a roer se ria.

O rato roeu a roupa do rei de roma

a rainha com raiva roeu o resto."""

print("Texto antigo: \n" +texto)
print("\n")
characters = ".,\n"
for x in range(len(characters)):
    texto = texto.replace(characters[x],"")
texto.split()

print("texto novo: \n" + texto)
print("\n")
texto = [texto.lower() for texto in texto]

import string
texto = [texto.strip(string.punctuation) for texto in texto]

vocabulario = set(texto)

vocabulario_ordenado = sorted(vocabulario)
print("Vocabulario :")
print(vocabulario_ordenado)

