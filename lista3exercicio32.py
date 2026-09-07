while True:
    numero = int(input('Digite um número (digite 0 para sair): '))
    if numero < 0:
        print(str(numero) + ' é negativo.')
    elif numero > 0:
        print(str(numero) + ' é positivo.')
    else:
        break