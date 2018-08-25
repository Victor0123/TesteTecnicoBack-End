salario = 1000.00
aumento_percentual = 0.015
ano_atual = 2018
ano_inicial = 2006

for i in range(ano_inicial, ano_atual + 1):
    salario = salario + (salario * aumento_percentual)
    aumento_percentual *= 2

print('Salario: %2.2f' %salario)
