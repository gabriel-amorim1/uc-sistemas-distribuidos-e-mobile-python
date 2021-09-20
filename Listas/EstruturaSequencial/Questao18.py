tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade do link de internet em Mbps: "))

tempo = (tamanho / velocidade) / 60

print("Tempo aproximado de download: ", round(tempo))