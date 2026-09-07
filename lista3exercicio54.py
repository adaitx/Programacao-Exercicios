while True:
    numero = int(input('Digite um número: '))
    if numero < 1 or numero > 10:
        print('Número de entrada inválido!')
    else:
        print('Número de entrada válido. Programa encerrado.')
        break