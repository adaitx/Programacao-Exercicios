compra = float(input('Digite o valor de sua compra: '))

if compra <= 50:
    print('O valor de sua compra é de R$' + str(compra) + '.')
elif compra <=200:
    compra = compra * 0.95
    print('O valor de sua compra é de R$' + str(compra) + '.')
elif compra <=500:
    compra = compra * 0.90
    print('O valor de sua compra é de R$' + str(compra) + '.')
elif compra > 500:
    compra = compra * 0.85
    print('O valor de sua compra é de R$' + str(compra) + '.')