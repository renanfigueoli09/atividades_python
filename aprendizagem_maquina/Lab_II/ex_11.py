valor_por_hora = float(input("Digite o valor da hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_bruto = valor_por_hora * horas_trabalhadas
if salario_bruto <= 900:
    ir_desconto = 0
elif salario_bruto <= 1500:
    ir_desconto = 5
elif salario_bruto <= 2500:
    ir_desconto = 10
else:
    ir_desconto = 20

ir_valor = (ir_desconto / 100) * salario_bruto
inss = 0.10 * salario_bruto
fgts = 0.11 * salario_bruto
total_descontos = ir_valor + inss
salario_liquido = salario_bruto - total_descontos
print(f"Salário Bruto: (R$ {valor_por_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_desconto}%): R$ {ir_valor:.2f}")
print(f"(-) INSS (10%): R$ {inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
