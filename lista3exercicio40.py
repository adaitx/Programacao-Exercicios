numero = int(input('Digite um número (0 para sair): '))
contador_p = 0
contador_n = 0

while numero != 0:
    if numero > 0:
        contador_p = contador_p + 1
    else:
        contador_n = contador_n + 1

    numero = int(input('Digite um número (0 para sair): '))

print()
print('Foram digitados ' + str(contador_p) + ' números positivos.')
print('Foram digitados ' + str(contador_n) + ' números negativos.')
print()