numeros = []
pares = []
impares = []
for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
