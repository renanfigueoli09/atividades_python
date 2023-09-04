notas = []
for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Notas digitadas:")
for nota in notas:
    print(nota)
print(f"Média das notas: {media:.2f}")
