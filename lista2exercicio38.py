mes = int(input('Digite um número de 1 a 12 representando o mês escolhido: '))

if 1 <= mes <=3:
    print('A estação é Verão! ')
elif mes <= 6:
    print('A estação é Outono! ')
elif mes <= 9:
    print('A estação é Inverno!')
elif mes <=12:
    print('A estação é Primavera!')