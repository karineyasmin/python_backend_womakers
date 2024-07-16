# 10. Faça um programa que lê três números inteiros e os mostra em ordem
# crescente.


num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

lista = [num1, num2, num3]
lista_ordenada = sorted(lista)

print("Números em ordem crescente: ", lista_ordenada)
