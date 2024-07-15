# 4. Receba do usuário a quantidade de litros de combustível consumidos e
# a distância percorrida. Calcule e imprima o consumo médio em km/l


qtd_litros = float(input("Quantidade de litros de combustível consumidos: "))

distancia_percorrida = float(input("Distância percorrida: "))

consumo_medio = distancia_percorrida / qtd_litros

print(f"O consumo médio foi de {consumo_medio} km/l")
