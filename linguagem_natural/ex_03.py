num = [int(n) for n in input("Digite uma lista de números separados por vírgulas: ").split(',')]

ma_num = num[0]
me_num = num[0]
for n in num:
    if n > ma_num:
        ma_num = n
    if n < me_num:
        me_num = n

print(f"numero maior: {ma_num}")
print(f"numero menor: {me_num}")   
