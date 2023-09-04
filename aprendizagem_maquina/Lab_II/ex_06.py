peso_peixes = float(input("Digite o peso de peixes (em quilos): "))
limite = 50
if peso_peixes > limite:
    excesso = peso_peixes - limite
    multa = excesso * 4
    print(f"Peso de peixes excedeu o limite em {excesso:.2f} quilos.")
    print(f"O valor da multa a ser pago é de R$ {multa:.2f}.")
else:
    print("Peso de peixes dentro do limite estabelecido. Não há multa a pagar.")
