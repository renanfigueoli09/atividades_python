num = int(input("escreva um número"))
a = 1103515245
c = 12345
m = 2**31

def gerar_numero_aleatorio(seed):
    seed = (a * seed + c) % m
    return seed

nums = []
for _ in range(100):
    num = gerar_numero_aleatorio(num)
    numero_aleatorio = num % 1000 + 1
    nums.append(numero_aleatorio)

print(nums)
