soma = 0

while True:
    n = int(input('Digite um número (digite 0 para sair): '))
    if n == 0:
        break
    soma = soma + n

print('A soma total dos números é ' + str(soma) + '.')