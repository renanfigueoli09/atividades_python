total_compra = 0
print("Lojas Tabajara")
contador = 1
while True:
    preco_produto = float(input(f"Produto {contador}: R$ "))
    
    # Verifica se o preço do produto é zero para finalizar a compra
    if preco_produto == 0:
        break
    
    total_compra += preco_produto
    contador += 1

dinheiro_cliente = float(input("Total: R$ {:.2f}\nDinheiro: R$ ".format(total_compra)))
troco = dinheiro_cliente - total_compra
print(f"Total: R$ {total_compra:.2f}")
print(f"Troco: R$ {troco:.2f}")