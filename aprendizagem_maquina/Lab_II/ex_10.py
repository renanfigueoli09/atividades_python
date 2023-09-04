salario_atual = float(input("Digite o salário atual do colaborador: R$ "))
percentual_aumento = 0
valor_aumento = 0
if salario_atual <= 280:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = (percentual_aumento / 100) * salario_atual
novo_salario = salario_atual + valor_aumento
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
