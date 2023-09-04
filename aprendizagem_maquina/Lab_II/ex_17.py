numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
menor_numero = min(numero1, numero2)
maior_numero = max(numero1, numero2)
print(f"Números no intervalo entre {menor_numero} e {maior_numero}:")
for numero in range(menor_numero, maior_numero + 1):
    print(numero)