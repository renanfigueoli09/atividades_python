notas = [[0] * 5 for _ in range(10)]
max_nota = float('-inf')
min_nota = float('inf')

for i in range(10):
    print(f"Notas do aluno {i + 1}:")
    for nota in range(5):
        notas[i][nota] = float(input(f"Nota {nota + 1}: "))


print("\nnotas:")

for i in range(10):
    print(f"Aluno {i + 1}: {notas[i]}")


for i in notas:
    for nota in i:
        if nota > max_nota:
            max_nota = nota
        if nota < min_nota:
            min_nota = nota

print(f"\nmaior nota: {max_nota}")
print(f"menor nota: {min_nota}")

print("\nMédias dos alunos:")
for i in notas:
    m = sum(i) / len(i)
    print(f"media: {m:.2f}")
