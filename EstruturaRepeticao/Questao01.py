nota = int(input("Digite uma nota entre 0 e 10: "))

while (nota < 0) or (nota > 10):
    print("Nota inválida")
    nota = int(input("Digite uma nota entre 0 e 10: "))