# 4. Crie um dicionário representando contatos (nome, telefone).
# Permita ao usuário procurar por um contato pelo nome.


contatos = {}

while True:
    nome = input("Digite o nome do contato (ou 'sair' para terminar): ").capitalize()
    if nome.lower() == "sair":
        break
    telefone = input("Digite o telefone do contato: ")
    contatos[nome] = telefone


nome_procurado = input("Digite o nome do contato que deseja procurar: ").capitalize()

if nome_procurado in contatos:
    print(f"Telefone de {nome_procurado}: {contatos[nome_procurado]}")
else:
    print(f"Contato {nome_procurado} não encontrado.")
