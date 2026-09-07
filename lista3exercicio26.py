soma = 0
quantidade = 0

for contador in range (5):
    numero = float(input('Digite o valor de um número: '))
    soma = soma + numero
    quantidade = quantidade + 1

media = soma / quantidade
print('A média entre esses números é ' + str(media) + '.')