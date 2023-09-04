numero = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

print(f"Fatorial de: {numero}")
print(f"{numero}! =", end=" ")
for i in range(1, numero):
    print(f"{i} . ", end="")
print(f"1 = {fatorial}")
