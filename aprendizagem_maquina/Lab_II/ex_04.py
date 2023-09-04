valor_por_hora = float(input("Digite o valor ganho por hora de trabalho: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_mensal = valor_por_hora * horas_trabalhadas
print(f"O seu salário no mês é: R$ {salario_mensal:.2f}")
