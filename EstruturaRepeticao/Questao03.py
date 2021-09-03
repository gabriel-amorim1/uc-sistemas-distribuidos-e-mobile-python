nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo: ")
estado_civil = input("Digite seu estado civil: ")

while (
    (len(nome) < 3)
    or (idade < 0) or (idade > 150)
    or (salario <= 0) 
    or ((sexo != 'f') and (sexo != 'm')) 
    or ((estado_civil != 's') and (estado_civil != 'c') and (estado_civil != 'v') and (estado_civil != 'd'))):
    print("Informações incorretas, digite novamente.")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    sexo = input("Digite seu sexo: ")
    estado_civil = input("Digite seu estado civil: ")