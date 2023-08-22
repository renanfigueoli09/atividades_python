num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numMenor = min(num1, num2, num3)

soma = num1 + num2 + num3 - numMenor

print(f"A soma dos dois maiores números é: {soma}")
