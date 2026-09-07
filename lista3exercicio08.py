n = int(input('Digite um número inteiro positivo: '))
digitos = 0

while n <= 0:
    print('Número inválido.')
    n = int(input('Digite um número inteiro positivo: '))

while n > 0:
    digitos = digitos + 1
    n = n // 10

print('O número possui ' + str(digitos) + ' dígitos.')