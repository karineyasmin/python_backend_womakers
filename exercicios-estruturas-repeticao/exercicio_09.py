# 9. O programa deve calcular e apresentar a quantidade de números pares e
# ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
# informar o valor zero. Certifique-se de incluir validações para garantir que
# apenas números positivos sejam considerados na contagem e cálculos.


entrada_usuario = None
total_pares = 0
total_impares = 0

while True:
    entrada_usuario = int(input("Digite um número: "))
    if entrada_usuario == 0:
        break

    if entrada_usuario > 0:
        if entrada_usuario % 2 == 0:
            total_pares += 1
        else:
            total_impares += 1

print(f"Você digitou {total_pares} números pares e {total_impares} números ímpares.")
