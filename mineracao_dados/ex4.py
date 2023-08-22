while True:
    n = int(input("Digite um valor numero maior que zero: "))
    if n > 0:
        break 
    else:
        print("O valor de numero deve ser maior que zero.")

for i in range(1, n+1):
    print(i)
