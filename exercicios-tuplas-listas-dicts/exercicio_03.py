# 3. Crie um dicionário representando um carrinho de compras.
# Adicione produtos (chaves) e quantidades (valores) ao carrinho.
# Calcule o total do carrinho de compra.

carrinho = {}

carrinho["arroz"] = 3
carrinho["feijã0"] = 2
carrinho["laranja"] = 12


total = sum(carrinho.values())

print("Carrinho de compras:", carrinho)
print("Total de itens no carrinho:", total)
