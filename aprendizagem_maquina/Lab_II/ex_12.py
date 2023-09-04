while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    else:
        print("Nome deve ter mais de 3 caracteres. Tente novamente.")

while True:
    idade = int(input("Digite sua idade (entre 0 e 150): "))
    if 0 <= idade <= 150:
        break
    else:
        print("Idade deve estar entre 0 e 150. Tente novamente.")

while True:
    salario = float(input("Digite seu salário (maior que zero): "))
    if salario > 0:
        break
    else:
        print("Salário deve ser maior que zero. Tente novamente.")

while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("Sexo deve ser 'f' ou 'm'. Tente novamente.")

while True:
    estado_civil = input("Digite seu estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").lower()
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    else:
        print("Estado civil deve ser 's', 'c', 'v' ou 'd'. Tente novamente.")


print("\nInformações validadas:")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
