contador = 0

for numero in range(2,101):
    primo = True
    for divisor in range (2, numero):
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        contador = contador + 1

print('O número total de números primos entre 1 e 100 é de ' + str(contador) + '.')