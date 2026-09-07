saldo = 0

while True:
    print('--- CAIXA ELETRÔNICO ---')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Sair')

    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        valor = float(input('Digite o valor do depósito: R$'))
        saldo = saldo + valor
        print()
        print('Depósito realizado!')
        print('Saldo atual: R$ ' + str(saldo))

    elif opcao == 2:
        print()
        valor = float(input('Digite o valor do saque: R$'))

        if valor <= saldo:
            saldo = saldo - valor
            print()
            print('Saque realizado!')
            print('Saldo atual: R$ ' + str(saldo))
        else:
            print('Saldo insuficiente! Transação cancelada')

    elif opcao == 3:
        print()
        print('Obrigado por utilizar o caixa eletrônico!')
        break

    else:
        print('Opção inválida!')

    print()