# 9. Faça um Programa que utilize 4 variáveis como preferir e no final print
# uma mensagem amigável utilizando as variáveis criadas.
# Exemplos de variáveis: nome, idade, lugar, profissão ....
# Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
# também e estou migrando de área.
# Lembrando que para o retorno vamos usar print com as variáveis
# criadas e este texto é somente um exemplo, utilizem a criatividade.


nome = input("Qual o seu nome? ")
origem = input("De onde você é? ")
cor = input("Qual sua cor favorita? ")
stack = input("Qual a sua stack? ")


print(
    f"Olá {nome}, você é de {origem}, que legal! \nEu sou de São Paulo. Sua cor favorita é {cor}? Acho que essa cor combina mesmo com você! \n Você é dev {stack}? ah, eu sou desenvolvedora Python."
)
