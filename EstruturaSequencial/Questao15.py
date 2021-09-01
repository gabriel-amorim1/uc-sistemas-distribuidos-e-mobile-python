valor_da_hora = float(input("Digite o valor da hora: "))

horas_trabalhadas_mes = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_da_hora * horas_trabalhadas_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

my_formatter = "{0:.2f}"

print("+ Salário bruto : R$ ", my_formatter.format(salario_bruto))
print("- IR (11%) : R$ ", my_formatter.format(ir))
print("- INSS (8%) : R$ ", my_formatter.format(inss))
print("- Sindicato (5%) : R$ ", my_formatter.format(sindicato))
print("= Salário Líquido : R$ ", my_formatter.format(salario_liquido))
