fatorial = 1
numero = (int(input('Digite um número inteiro: ')))

if numero < 0:
    print('Não existe fatorial de número negativo.')
elif numero == 0:
    print('O fatorial de ' + str(numero) + ' é ' + str(fatorial) + '.')
else:
    for contador in range(1, numero + 1):
        fatorial = fatorial * contador

    print('O fatorial de ' + str(numero) + ' é ' + str(fatorial) + '.')