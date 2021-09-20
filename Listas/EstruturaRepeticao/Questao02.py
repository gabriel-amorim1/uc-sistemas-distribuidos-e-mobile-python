nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while (nome == senha):
    print("A senha não pode ser igual ao nome, por favor digite as informações novamente.")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")