# 5. Desenvolva um programa que solicite ao usuário os comprimentos dos três
# lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.

lado1 = float(input("Comprimento do primeiro lado -> "))
lado2 = float(input("Comprimento do segundo lado -> "))
lado3 = float(input("Comprimento do terceiro lado -> "))

equilatero = lado1 == lado2 == lado3

isosceles = lado1 == lado2 or lado1 == lado3 or lado2 == lado3

escaleno = lado1 != lado2 != lado3


if equilatero:
    print("É um triângulo equilátero!")
elif isosceles:
    print("É um triângulo isósceles!")
elif escaleno:
    print("É um triângulo escaleno!")
else:
    print("Formato não reconhecido")
