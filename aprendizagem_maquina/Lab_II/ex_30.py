def soma_três_numeros(a, b, c):
    return a + b + c

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
resultado = soma_três_numeros(numero1, numero2, numero3)
print(f"A soma dos três números é: {resultado}")