# 6. Vamos construir um jogo de forca. O programa escolherá
# aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
# secreta será representada por espaços em branco, um para cada letra
# da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
# tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
# na palavra secreta, ela será revelada nas posições correspondentes. Se
# a letra não estiver na palavra, uma mensagem de erro deverá ser
# informada. Após um número máximo de erros, o jogador perde. O jogo
# continua até que o jogador adivinhe a palavra ou exceda o número
# máximo de tentativas.
# Dica: Você precisará importar uma biblioteca para resolver esse
# exercício

import random


def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]
    return random.choice(palavras)


def mostrar_palavra(palavra_secreta, letras_adivinhadas):
    return " ".join(
        [letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta]
    )


def jogo_forca():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_erradas = 0
    max_tentativas = 6

    print("Bem-vindo ao jogo da forca!")

    while tentativas_erradas < max_tentativas:
        estado_atual = mostrar_palavra(palavra_secreta, letras_adivinhadas)
        print(f"\nPalavra: {estado_atual}")
        print(f"Tentativas restantes: {max_tentativas - tentativas_erradas}")

        letra = input("Adivinhe uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra.")
            continue

        letras_adivinhadas.add(letra)

        if letra in palavra_secreta:
            print("Boa! A letra está na palavra.")
        else:
            print("Errado! A letra não está na palavra.")
            tentativas_erradas += 1

        if all(letra in letras_adivinhadas for letra in palavra_secreta):
            print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}")
            break
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")


jogo_forca()
