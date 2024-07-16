# 7. Desenvolver um programa que solicite a idade do usuário e identifique se
# ele é uma criança, um adolescente, adulto ou idoso.


idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Você é criança!")
elif idade >= 12 and idade < 18:
    print("Você é adolescente!")
elif idade >= 18 and idade < 65:
    print("Você é adulto(a)!")
else:
    print("Você é idoso(a)!")
