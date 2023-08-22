while True:
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor (não pode ser zero): "))
    
    if v2 != 0:
        break 
    else:
        print("O segundo valor não pode ser zero.")

res = v1 / v2
print(f"Resultado da divisão: {res}")