# 3. Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

nota = int(input("Por favor, digite uma nota (0-10) -> "))


while True:
    if nota >= 0 and nota <= 10:
        print(f"Nota: {nota}")
        break
    else:
        print("Valor inválido!")
        nota = int(input("Por favor, Digite uma nota (0-10) -> "))
