usuario_correto = 'admin'
senha_correta = '123fatec'
tentativas = 3

while tentativas > 0:
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')

    if usuario == usuario_correto:
        if senha == senha_correta:
            print('Acesso liberado!')
            break
        else:
            tentativas = tentativas - 1
            print('Senha incorreta!')
            print('Número de tentativas restantes: ' + str(tentativas))
    else:
        tentativas = tentativas - 1
        print('Usuário incorreto!')
        print('Número de tentativas restantes: ' + str(tentativas))

if tentativas == 0:
    print('Acesso bloqueado!')