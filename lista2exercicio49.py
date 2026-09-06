temperatura = float(input('Digite a temperatura: '))
umidade = int(input('Digite a umidade do ar (em %): '))

if temperatura > 30:
    if umidade < 30:
        print('Alerta de incêndio!')
    else:
        print('Calor, mas sem risco de incêndio.')
else:
    print('Temperatura baixa.')