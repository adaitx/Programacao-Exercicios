contador = 1
soma = 0

while contador <= 5:
    n = int(input('Digite um número: '))
    soma = soma + n
    contador = contador + 1

print('A soma total dos números é ' + str(soma) + '.')