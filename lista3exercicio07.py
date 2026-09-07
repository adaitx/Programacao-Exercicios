senha_verdadeira = '123fatec'
senha = input('Digite sua senha: ')

while senha != senha_verdadeira:
    print('Acesso negado! ')
    senha = input('Digite novamente: ')

print('Acesso liberado! ')