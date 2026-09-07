while True:
    idade = int(input('Digite a idade desejada (-1 para sair): '))

    if idade < -1 or idade == 0:
        print('Número não aceito.')
        print()
    elif idade == -1:
        print()
        break
    elif idade < 18:
        print('A pessoa é menor de idade.')
        print()
    else:
        print('A pessoa é maior de idade')
        print()