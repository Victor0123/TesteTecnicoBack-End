metros_quadrados = int(input('Metros quadrados: '))
litros_metros = 54
preco_lata = 80
quant_latas = metros_quadrados // 54
if metros_quadrados % 54 > 0:
    quant_latas += 1

total_pagar = quant_latas * preco_lata

print('Seram usadas {} latas de tinta e pagara {} reais nas latas'.format(quant_latas, total_pagar))
