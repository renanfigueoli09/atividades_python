def calcular_fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * calcular_fatorial(num - 1)

num = int(input("Digite um número para calcular o fatorial: "))
res = calcular_fatorial(num)
print(f"O fatorial de {num} é: {res}")
