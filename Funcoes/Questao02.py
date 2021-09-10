def imprime_valor_n_n_vezes(n):
    for i in range(n):
        i += 1
        linha = ""

        for j in range(i):
            j += 1
            linha += str(j) + " "

        print(linha)
        linha = ""


n = int(input("Digite um valor inteiro: "))

imprime_valor_n_n_vezes(n)
