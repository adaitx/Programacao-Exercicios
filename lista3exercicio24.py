contador = 0

for numero in range (1,51):
    if numero % 2 == 0:
        contador = contador + 1

print('Existem ' + str(contador) + ' números pares entre 1 e 50.')