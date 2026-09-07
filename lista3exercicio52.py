estoque = 100

print()
print('Nosso estoque é de ' + str(estoque) + ' unidades.')
while True:
    unidade = int(input('Quantas unidades foram vendidas? '))

    if unidade <= 0:
        print()
        print('Quantidade inválida.')

    elif unidade > estoque:
        print()
        print('O número de vendas é maior que o estoque disponível. ')
    elif unidade == estoque:
        estoque = estoque - unidade
        print()
        print('Todas as unidades foram vendidas! ')
        break
    else:
        estoque = estoque - unidade
        print()
        print('O número de unidades restantes é de ' + str(estoque) + '.')