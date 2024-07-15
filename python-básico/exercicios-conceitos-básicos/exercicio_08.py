# 8. Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma
# média de 5 calorias por minuto de exercício.


horas_exercicio_semanal = float(input("Horas de exercício por semana: "))
horas_exercicio_mensal = horas_exercicio_semanal * 4
total_minutos = horas_exercicio_mensal * 60
media_calorias_minuto = 5

total_calorias = media_calorias_minuto * total_minutos


print(f"Total de calorias queimadas no mês: {total_calorias:.2f}")
