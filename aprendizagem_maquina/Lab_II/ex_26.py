caracteres = []
for i in range(10):
    caractere = input(f"Digite o {i + 1}º caractere: ")
    caracteres.append(caractere)

consoantes = "bcdfghjklmnpqrstvwxyz"
contador_consoantes = 0
consoantes_lidas = []
for caractere in caracteres:
    if caractere.lower() in consoantes:
        contador_consoantes += 1
        consoantes_lidas.append(caractere)

print(f"Foram lidas {contador_consoantes} consoantes.")
print("Consoantes lidas:", ", ".join(consoantes_lidas))
