num = int(input("escreva um número"))
def num_ale(i):
    i = (1103515245 * i + 12345) % (2**31)
    return i

nums = []
for _ in range(100):
    num = num_ale(num)
    numero_aleatorio = num % 1000 + 1
    nums.append(numero_aleatorio)

print(nums)
