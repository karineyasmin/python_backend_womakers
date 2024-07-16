# 8. Criar um programa em Python que solicite três números ao usuário, utilize
# estruturas condicionais para determinar o maior entre eles e apresente o
# resultado.

print("Digite três números para saber qual é o maior deles")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f"O maior número é: {maior}")
