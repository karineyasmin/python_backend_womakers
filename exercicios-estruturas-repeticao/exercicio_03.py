# 3. Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

while True:
    try:
        nota = int(input("Por favor, digite uma nota (0-10) -> "))
        if 0 <= nota <= 10:
            print(f"Nota: {nota}")
            break
        else:
            print("Valor inválido! A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
