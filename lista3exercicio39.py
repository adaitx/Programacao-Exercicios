contador = 0

for numero in range(1,101):
    if numero % 7 == 0:
        contador = contador + 1

print('Existem ' + str(contador) + ' múltiplos de 7 no intervalo de 1 a 100.')