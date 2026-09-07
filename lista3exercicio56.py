import random

while True:
    computador = random.randint(1, 10)
    usuario = int(input('Digite um número: '))
    escolha = input('Você escolhe par ou ímpar? ')

    soma = usuario + computador

    if soma % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'ímpar'

    if escolha == resultado:
        print()
        print('O computador escolheu ' + str(computador) + '.')
        print('O total é de ' + str(soma) + '.')
        print('Você venceu!')
        print()
    else:
        print()
        print('O computador escolheu ' + str(computador) + '.')
        print('O total é de ' + str(soma) + '.')
        print('O computador venceu!')
        print()

    continuar = input('Deseja jogar novamente? (S/N) ')

    if continuar == 'N':
        break