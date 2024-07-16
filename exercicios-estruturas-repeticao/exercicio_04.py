# 4. Implemente um programa que classifique um aluno com base em sua
# pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10.
# Se pontuação for maior ou igual a 7, o aluno é aprovado; ]
# caso contrário, é reprovado.


nota = float(input("Digite a nota (0-10): "))


if nota >= 7:
    print("Aprovado(a)!")
else:
    print("Reprovado(a)!")
