compra = float(input('Digite o valor de sua compra: '))

if compra > 100:
    print('Desconto liberado! ')
    compra = compra - (compra*0.1)
    print('O valor de sua compra é R$' + str(compra) + '.')
else:
    print('O valor de sua compra é R$' + str(compra) + '.')