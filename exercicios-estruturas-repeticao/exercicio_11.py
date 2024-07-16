# 11. Escreva um programa que calcule o salário líquido.
# Lembrando de declarar o salário bruto e o percentual de desconto do Imposto% de Renda.
# ● Renda até R$ 1.903,98: isento de imposto de renda;
# ● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
# ● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
# ● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
# ● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%


salario_bruto = float(input("Digite o salário: R$ "))
imposto = 0.00
salario_liquido = salario_bruto - (salario_bruto / 100) * imposto
salario_final = f"Salário Bruto: R$ {salario_bruto:.2f}\nPercentual de desconto: {imposto}%\nSalário líquido: R$ {salario_liquido:.2f}"
print()

if salario_bruto <= 1_903.98:
    imposto = 0.00
    print("Isento de imposto.")
    print(salario_final)

elif salario_bruto >= 1_903.98 and salario_bruto <= 2_826.65:
    imposto = 7.5
    salario_liquido = salario_bruto - (salario_bruto / 100) * imposto
    salario_final = f"Salário Bruto: R$ {salario_bruto:.2f}\nPercentual de desconto: {imposto}%\nSalário líquido: R$ {salario_liquido:.2f}"
    print(salario_final)

elif salario_bruto >= 2_826.66 and salario_bruto <= 3_751.05:
    imposto = 15
    salario_liquido = salario_bruto - (salario_bruto / 100) * imposto
    salario_final = f"Salário Bruto: R$ {salario_bruto:.2f}\nPercentual de desconto: {imposto}%\nSalário líquido: R$ {salario_liquido:.2f}"
    print(salario_final)

elif salario_bruto >= 3_751.06 and salario_bruto <= 4_664.68:
    imposto = 22.5
    salario_liquido = salario_bruto - (salario_bruto / 100) * imposto
    salario_final = f"Salário Bruto: R$ {salario_bruto:.2f}\nPercentual de desconto: {imposto}%\nSalário líquido: R$ {salario_liquido:.2f}"
    print(salario_final)

else:
    imposto = 27.5
    salario_liquido = salario_bruto - (salario_bruto / 100) * imposto
    salario_final = f"Salário Bruto: R$ {salario_bruto:.2f}\nPercentual de desconto: {imposto}%\nSalário líquido: R$ {salario_liquido:.2f}"
    print(salario_final)
