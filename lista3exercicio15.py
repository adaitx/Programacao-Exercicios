soma = 0

while True:
    valor = float(input('Digite o valor do depósito (digite 0 para sair): '))

    if valor == 0:
        break
    if valor < 0:
        print('Número inválido.')
    else:
        soma = soma + valor

print('O saldo total acumulado é de R$ ' + str(soma) + '.')