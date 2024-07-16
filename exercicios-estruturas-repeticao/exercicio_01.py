# 1. Faça um Programa que peça dois números e imprima o maior deles


numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))


if numero1 > numero2:
    maior = numero1
elif numero1 < numero2:
    maior = numero2
else:
    print("Os números são iguais.")


print(f"O maior número é o {maior}.")
