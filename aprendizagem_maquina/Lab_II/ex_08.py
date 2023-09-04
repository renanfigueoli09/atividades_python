letra = input("Digite uma letra: ")
if letra.isalpha() and len(letra) == 1:
    letra = letra.lower()
    if letra in "aeiou":
        print("A letra digitada é uma vogal.")
    else:
        print("A letra digitada é uma consoante.")
else:
    print("Por favor, digite uma única letra do alfabeto.")
