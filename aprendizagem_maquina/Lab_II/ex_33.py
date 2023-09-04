def converter_hora(hora, minutos):
    if hora >= 12:
        periodo = 'P.M.'
        if hora > 12:
            hora -= 12
    else:
        periodo = 'A.M.'
        if hora == 0:
            hora = 12
    return hora, minutos, periodo

def exibir_hora(hora, minutos, periodo):
    print(f"A hora convertida é: {hora}:{minutos:02d} {periodo}")

while True:
    try:
        hora = int(input("Digite a hora (0-23): "))
        minutos = int(input("Digite os minutos (0-59): "))

        if 0 <= hora <= 23 and 0 <= minutos <= 59:
            hora_convertida, minutos_convertidos, periodo = converter_hora(hora, minutos)
            exibir_hora(hora_convertida, minutos_convertidos, periodo)
        else:
            print("Por favor, insira valores válidos para a hora (0-23) e os minutos (0-59).")

        repetir = input("Deseja converter outra hora? (sim ou não): ").strip().lower()
        if repetir != "sim":
            break
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
