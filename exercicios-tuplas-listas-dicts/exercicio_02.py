# 2. Faça um Programa que peça as quatro notas de 5 alunos, calcule
# e armazene numa lista a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.

medias = []


for aluno in range(5):
    print(f"Aluno {aluno + 1}: ")
    notas = []

    for n in range(4):
        nota = float(input(f"Digite a nota {n + 1}: "))
        notas.append(nota)

    media = sum(notas) / 4
    medias.append(media)

alunos_acima_7 = sum(1 for media in medias if media >= 7.0)
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_acima_7}")
