primeiro_inteiro = int(input("Digite o primeiro número inteiro: "))
segundo_inteiro = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

a = (primeiro_inteiro * 2) * (segundo_inteiro / 2)
b = (primeiro_inteiro * 3) + num_real
c = pow(num_real, 3)

print("a. O produto do dobro do primeiro com metade do segundo: ", a)
print("b. A soma do triplo do primeiro com o terceiro: ", b)
print("c. O terceiro elevado ao cubo: ", c)