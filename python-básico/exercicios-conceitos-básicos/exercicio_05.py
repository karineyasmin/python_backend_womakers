# 5. Escreva um programa que calcule o tempo de uma viagem. Faça um
# comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração:
# ● avião = 600 km/h
# ● carro = 100 km/h
# ● ônibus = 80 km/h


tempo_viagem = float(input("Distância da viagem em km: "))

aviao = tempo_viagem / 600
carro = tempo_viagem / 100
onibus = tempo_viagem / 80


print(f"Tempo da viagem em avião é de {aviao:.2f} horas")
print(f"Tempo da viagem em carro é de {carro:.2f} horas")
print(f"Tempo da viagem em ônibus é de {onibus:.2f} horas")
