senha_correta = '123fatec'
tentativas = 3

while tentativas > 0:
    senha = input('Digite sua senha: ')
    if senha == senha_correta:
        print()
        print('Acesso liberado!')
        break
    else:
        tentativas = tentativas - 1
        if tentativas == 1:
            print()
            print('Senha incorreta! Resta 1 tentativa.')
        elif tentativas > 1:
            print()
            print('Senha incorreta! Restam ' + str(tentativas) + ' tentativas.')
        else:
            print()
            print('Você atingiu o limite de tentativas. Bloqueado. ')