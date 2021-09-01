peso = float(input("Digite o peso dos peixes em quilos: "))

excesso = peso - 50

multa = excesso * 4

print("Excesso de peso: ", excesso)
print("Multa: R$ %.2f" %multa)