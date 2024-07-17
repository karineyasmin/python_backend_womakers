# 1. Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime.
# As perguntas são:
# ""Telefonou para a vítima?""
# ""Esteve no local do crime?""
# ""Mora perto da vítima?""
# ""Devia para a vítima?""
# ""Já trabalhou com a vítima?""
# O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
# ""Assassino"".
# Caso contrário,ele será classificado como""Inocente"".


lista_perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
]

lista_respostas = []
contador = 0
situacao = ""

print("Responda com S ou N")
for pergunta in lista_perguntas:
    resposta = input(f"{lista_perguntas[contador]} ").lower()
    lista_respostas.append(resposta)
    contador += 1

contador_sim = lista_respostas.count("s")
contador_nao = lista_respostas.count("n")


if contador_sim >= 2:
    situacao = "Suspeita"
elif contador_sim >= 3 and contador_sim <= 4:
    situacao = "Cúmplice"
elif contador == 5:
    situacao = "Assassino"
else:
    situacao = "Inocente"

print(f"\nVocê é {situacao}")
