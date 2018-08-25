horas_trabalhadas = int(input('Digite o valor das horas: '))
salario_minimo = float(input('Digite o salario: '))
valor_hora_bruto   = salario_minimo / horas_trabalhadas
valor_hora_liquida = valor_hora_bruto - (valor_hora_bruto * 0.1)
salario_bruto = valor_hora_liquida * horas_trabalhadas
taxa_imposto = 0.03
imposto = salario_bruto * taxa_imposto
salario_receber = salario_bruto - imposto

print("{0:.2f}".format(salario_receber))
