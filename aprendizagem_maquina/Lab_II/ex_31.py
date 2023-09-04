def verifica_positivo_negativo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

numero = float(input("Digite um número: "))
resultado = verifica_positivo_negativo(numero)
print(f"O resultado é: {resultado}")
