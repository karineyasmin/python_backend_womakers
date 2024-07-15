# 3. Faça um Programa que peça a quantidade de quilômetros, transforme
# em metros, centímetros e milímetros.

quilometros = float(input("Quilômetros: "))


conversao_metros = quilometros * 1000
conversao_centimetros = quilometros * 100_000
conversao_milimetros = quilometros * 1_000_000


print(f"{quilometros} quilômetros = {conversao_metros} metros")
print(f"{quilometros} quilômetros = {conversao_centimetros} centímetros")
print(f"{quilometros} quilômetros = {conversao_milimetros} milímetros")
