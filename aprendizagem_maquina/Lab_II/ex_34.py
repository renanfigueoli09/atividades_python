def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso <= 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        return valor_prestacao + multa + juros

total_prestacoes = 0
valor_total_pago = 0

while True:
    valor_prestacao = float(input("Digite o valor da prestação (ou zero para encerrar): "))
    if valor_prestacao == 0:
        break
    
    dias_atraso = int(input("Digite o número de dias em atraso: "))
    
    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)
    
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")
    
    total_prestacoes += 1
    valor_total_pago += valor_a_pagar

print(f"Relatório do dia:")
print(f"Quantidade de prestações pagas: {total_prestacoes}")
print(f"Valor total pago: R$ {valor_total_pago:.2f}")
