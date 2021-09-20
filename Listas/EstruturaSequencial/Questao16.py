import math

tamanho = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

quantidade = math.ceil((tamanho / (3 * 18)))
preco_total = quantidade * 80

print("Quantidade de latas de tinta: ", quantidade)
print("Preço total: R$ %.2f" %preco_total)