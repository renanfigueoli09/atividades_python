numMaior = float('-inf')

while True:
    num = float(input("Digite um número (0 para sair): "))
    
    if num == 0:
        break
    
    if num > numMaior:
        numMaior = num
        
print(f"O maior número digitado é: {numMaior}")