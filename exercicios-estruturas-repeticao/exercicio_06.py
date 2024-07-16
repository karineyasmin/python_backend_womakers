# 6. Crie um programa que solicite ao usuário um login e uma senha.
# O programa deve permitir o acesso apenas se o usuário for "admin" e a senha
# for "admin123", caso contrário imprima uma mensagem de erro.


usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "admin123":
    print("Login feito com sucesso!")
else:
    print("Usuário ou senha incorretos!")
