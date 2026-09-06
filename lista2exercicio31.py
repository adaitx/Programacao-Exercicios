n1 = int(input('Digite um primeiro número: '))
n2 = int(input('Digite um segundo número (deve ser diferente do primeiro): '))

if n1 > n2:
    print(str(n1) + ' é maior que ' + str(n2) + '!')
else:
    print(str(n2) + ' é maior que ' + str(n1) + '!')