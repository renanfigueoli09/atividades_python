perguntas = [
    "Telefonou?",
    "Esteve no local?",
    "Morava perto?",
    "Devia?",
    "Já trabalhou com a vítima?"
]

respostas_positivas = 0
for pergunta in perguntas:
    resposta = input(f"{pergunta} (sim ou não): ").strip().lower()
    if resposta == "sim":
        respostas_positivas += 1

if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"Classificação: {classificacao}")
