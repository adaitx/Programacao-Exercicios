minutos = int(input('Digite a quantidade de minutos utilizados em seu plano de celular: '))


if minutos <= 100:
    print('Você deverá pagar o valor de R$' + str(minutos*0.25) + '.')
elif minutos <=300:
    print('Você deverá pagar o valor de R$' + str(minutos*0.2) + '.')
elif minutos <=500:
    print('Você deverá pagar o valor de R$' + str(minutos*0.15) + '.')
else:
    print('Voce deverá pagar o valor de R$' + str(minutos*0.1) + '.')