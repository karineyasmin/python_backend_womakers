# 5. Crie uma função chamada contar_vogais que recebe uma string
# como parâmetro. Implemente a lógica para contar o número de vogais
# na string e retorne o total de vogais. Solicite ao usuário para inserir uma
# frase e utilize a função para contar as vogais.

VOGAIS = ["a", "e", "i", "o", "u"]


def contar_vogais(palavra):
    total_vogais = 0

    for letra in palavra:
        if letra in VOGAIS:
            total_vogais += 1

    return total_vogais


def main():
    print("=-=-= Contador de Vogais =-=-= ")

    while True:

        palavra = str(input("\nDigite uma palavra: ")).lower().strip()

        if len(palavra) <= 0:
            print("Você não digitou uma palavra!")
        else:
            total_vogais = contar_vogais(palavra)
            break

    print(f"\nA palavra {palavra} tem {total_vogais} vogais")


main()
