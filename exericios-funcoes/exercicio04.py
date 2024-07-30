# 4. Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
# Considere a tabela de conversão abaixo:
# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02
# Dólar Australiano: R$ 3,18
# Dólar Canadense: R$ 3,64
# Franco Suiço: R$ 0,42
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21

moedas = {
    "Euro": 5.36,
    "Franco Suiço": 0.42,
    "Peso Argentino": 0.02,
    "Dólar Americano ": 4.91,
    "Libra Esterlina": 6.21,
}


def menu():
    while True:
        try:

            print("=-=-= Conversor de Moedas =-=-=\n")
            print("Cotação do dia\n")
            for moeda, cotacao in moedas.items():
                print(f"{moeda:<18}{cotacao}")
            valor = float(input("\nDigite o valor para conversão R$ "))

            if valor < 1:
                print("\nPor favor, digite um valor acima de R$ 1\n")
            else:
                exibir_tabela(valor)
                break
        except ValueError:
            print("\nValor inválido! Digite somente valores númericos.\n")
            print("Pressione qualquer tecla para continuar")
            input()


def exibir_tabela(valor):
    print(f"\nCom R${valor:.2f} você pode comprar:\n")
    for moeda, cotacao in moedas.items():
        print(f"{moeda:<18} {valor * cotacao:.2f}")


menu()
