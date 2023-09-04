preco_do_pao = float(input("Digite o preço do pão: R$ "))
print("Panificadora Pão de Ontem - Tabela de preços")
for num_paes in range(1, 51):
    valor_total = num_paes * preco_do_pao
    print(f"{num_paes} - R$ {valor_total:.2f}")