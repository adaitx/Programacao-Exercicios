n1 = int(input('Digite um primeiro número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite um terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print('O maior número é ' + str(n1) + '.')
    else:
        print('O maior número é ' + str(n3) + '.')
else:
    if n2 > n3:
        print('O maior número é ' + str(n2) + '.')
    else:
        print('O maior número é ' + str(n3) + '.')