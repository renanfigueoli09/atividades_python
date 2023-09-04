def cont(numero):
    numero_str = str(numero)
    quantidade_digitos = len(numero_str)
    return quantidade_digitos

numero = int(input("Digite um número inteiro: "))
quantidade = cont(numero)
print(f"O número {numero} tem {quantidade} dígito(s).")
