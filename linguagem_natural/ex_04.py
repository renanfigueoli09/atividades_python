num = []
for i in range(10):
    if i == 0:
        num1 = int(input(f"escreva um número: "))
    else:
        num1 = int(input(f"escreva outro número: "))
    
    if i == 9:
        num1 = int(input(f"escreva o ultimo número: "))

    num.append(num1)


for i in range(len(num)):
    m = i
    for j in range(i+1, len(num)):
        if num[j] > num[m]:
            m = j
    num[i], num[m] = num[m], num[i]

print("ordem decrescente dos números digitados:")
for i in num:
    print(i)
