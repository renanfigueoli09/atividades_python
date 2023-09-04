soma = 0
nums = 5
for i in range(nums):
    num = float(input(f"Digite o {i + 1}º número: "))
    soma += num

media = soma / nums
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media:.2f}")