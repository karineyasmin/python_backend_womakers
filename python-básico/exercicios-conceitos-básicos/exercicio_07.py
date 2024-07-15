# 7. Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês.Calcule e mostre o total do seu
# salário no referido mês.


salario_hora = float(input("Salário por hora: "))
horas_trabalhadas = float(input("Horas trabalhadas: "))


salario = salario_hora * horas_trabalhadas

print(f"O salário do mês é de R${salario:.2f}")
