# 1. Faça um Programa que peça dois números, realize as principais
# operações soma, subtração, multiplicação, divisão


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print()
print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {subtracao}")
print(f"{numero1} * {numero2} = {multiplicacao}")
print(f"{numero1} / {numero2} = {divisao}")
