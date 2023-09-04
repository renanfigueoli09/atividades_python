def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)  # Calcula o valor do imposto
    custo_com_imposto = custo + imposto    # Calcula o custo com imposto
    return custo_com_imposto

taxa = float(input("Digite a taxa de imposto (em porcentagem): "))
custo_item = float(input("Digite o custo do item antes do imposto: R$ "))

custo_com_imposto = somaImposto(taxa, custo_item)
print(f"O custo do item com imposto é: R$ {custo_com_imposto:.2f}")
