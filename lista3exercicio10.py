contador = 0

while True:
    numero = int(input('Digite um número positivo (digite um número negativo para sair): '))
    if numero < 0:
        break
    if numero > 0:
        contador = contador + 1

print('Foram digitados ' + str(contador) + ' números positivos.')