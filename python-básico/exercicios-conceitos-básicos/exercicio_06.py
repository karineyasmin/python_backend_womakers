# 6. Solicite ao usuário o peso em kg e a altura em metros. Calcule e
# imprima o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura)

print("Calculadora de IMC")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura * altura)

print(f"O IMC é de {imc:.2f}")
