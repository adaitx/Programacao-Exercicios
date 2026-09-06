salario = float(input('Digite o seu salário (em R$): '))
tempo = int(input('Digite o tempo de trabalho (em anos): '))

if salario < 2000:
    if tempo >= 5:
        print('Elegível a reajuste. ')
    else:
        print('Tempo de serviço insuficiente.')
else:
    print('Salário muito alto.')