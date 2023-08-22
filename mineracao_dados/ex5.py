soma = 0
numero = int(input("Digite um valor numero: "))

while numero <= 1000:
    soma += numero
    numero += 1

print(f"A soma dos números positivos menores ou iguais a 1000 é: {soma}")
