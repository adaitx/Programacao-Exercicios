compra = float(input('Digite o valor da sua compra: '))
tipo_compra = input ('Digite a forma de pagamento (dinheiro ou cartão): ')

if tipo_compra == 'dinheiro':
    compra = compra * 0.90
    print('O valor de sua compra é R$' + str(compra) + '.')

elif tipo_compra == 'cartão':
    parcelas = int(input('Em quantas parcelas você deseja pagar? '))
    if parcelas > 3:
        print()
        print('Haverá uma cobrança de juros de 2 por cento ao mês')
        compra = compra + (compra * 0.02 * parcelas)
        print('O valor de sua compra é de R$' + str(compra) + '.')
        print('O valor de cada parcela é de R$' + str(compra/parcelas) + '.')
    else:
        print()
        print('Não haverá uma cobrança de juros.')
        print('O valor de sua compra é de R$' + str(compra) + '.')