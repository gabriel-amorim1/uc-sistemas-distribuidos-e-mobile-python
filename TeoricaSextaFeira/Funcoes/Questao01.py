def imprime_valor_n_n_vezes(n):
    for i in range(n):
        i += 1
        print((str(i) + " ") * i)


n = int(input("Digite um valor inteiro: "))

imprime_valor_n_n_vezes(n)
