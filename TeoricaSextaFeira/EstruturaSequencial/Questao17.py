import math

tamanho = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

quantidade_lata = math.ceil((tamanho / (6 * 18)))
preco_total_lata = quantidade_lata * 80

quantidade_galao = math.ceil((tamanho / (6 * 3.6)))
preco_total_galao = quantidade_galao * 25

my_formatter = "{0:.2f}"

print("Quantidade de latas de tinta: ", quantidade_lata)
print("Preço total: R$ ", my_formatter.format(preco_total_lata))

print("\nQuantidade de galões de tinta: ", quantidade_galao)
print("Preço total: R$ ", my_formatter.format(preco_total_galao))

tamanho_com_folga = tamanho * 1.1
if (((tamanho_com_folga % (6 * 18)) != 0) & (tamanho_com_folga > float(6 * 18))):
    quantidade_lata_misturada = math.floor(tamanho_com_folga / (6 * 18))
    restante_tinta = tamanho_com_folga % (6 * 18)
    quantidade_galao_misturada = math.ceil(restante_tinta / (6 * 3.6))
    preco_total_lata_misturado = quantidade_lata_misturada * 80
    preco_total_galao_misturado = quantidade_galao_misturada * 25
    preco_total_misturado = preco_total_lata_misturado + preco_total_galao_misturado

    print("\nLatas e galões misturados: ")
    print("Quantidade de latas de tinta: ", quantidade_lata_misturada)
    print("Preço das latas: R$ ", my_formatter.format(preco_total_lata_misturado))
    print("Quantidade de galões de tinta: ", quantidade_galao_misturada)
    print("Preço dos galões: R$ ", my_formatter.format(preco_total_galao_misturado))
    print("Preço total: R$ ", my_formatter.format(preco_total_misturado))