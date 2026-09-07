for contador in range (1,11):
    numero = int(input('Digite um número: '))

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

print()
print('O maior número é ' + str(maior) + '.')
print('O menor número é ' + str(menor) + '.')