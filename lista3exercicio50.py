gasto = 0

while True:
    compras = float(input('Digite o valor de sua compra (ou -1 para sair): '))

    if compras == -1:
        print()
        print('Compras encerradas!')
        break
    elif compras < 0:
        print('Valor inválido.')
    else:
        gasto = gasto + compras

if gasto == 0:
    print('Nenhuma compra foi realizada.')
elif gasto >= 1000:
    valor_final = gasto * 0.9
    print('Você ganhou desconto de 10% nas suas compras!')
    print('Valor: R$ ' + str(valor_final) + '.')
elif gasto >= 500:
    valor_final = gasto * 0.95
    print('Você ganhou desconto de 5% nas suas compras!')
    print('Valor: R$ ' + str(valor_final) + '.')
else:
    valor_final = gasto
    print('Você não obteve desconto nas suas compras.')
    print('Valor: R$ ' + str(gasto) + '.')