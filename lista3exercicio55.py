contador = 0

for semana in range(1,8):
    temperatura = float(input('Digite a temperatura do dia: '))

    if temperatura > 30:
        contador = contador + 1

print('A temperatura foi maior que 30 graus em ' + str(contador) + ' dias.')