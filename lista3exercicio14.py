soma = 0
numero = int(input('Digite um número inteiro positivo: '))

while numero <= 0:
    print('Número inválido. ')
    numero = int(input('Digite um número inteiro positivo: '))

while numero > 0:
    digito = numero % 10
    soma = soma + digito
    numero = numero // 10

print('A soma dos dígitos desse número é ' + str(soma) + '.')