while True:
    nomes = input("Digite o nome do atleta (ou deixe em branco para encerrar): ").strip()

    if nomes == "":
        break

    saltos = []

    for i in range(1, 6):
        salto = float(input(f"{i}º Salto: "))
        saltos.append(salto)

    media = sum(saltos) / len(saltos)

    print("Resultado final:")
    print(f"Atleta: {nomes}")
    print(f"Saltos: {' - '.join(map(str, saltos))}")
    print(f"Média dos saltos: {media:.1f} m")
