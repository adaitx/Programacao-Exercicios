n = int(input('Digite um número: '))
fatorial = 1

while n < 0:
    print('Não existe fatorial de números negativos. ')
    n = int(input('Digite um número: '))

contador = n

while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1

print('O fatorial desse número é ' + str(fatorial) + '.')