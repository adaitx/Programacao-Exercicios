for numero in range(1,31):
    if numero % 3 == 0 and numero % 5 == 0:
        print(str(numero) + ' múltiplo de 3 e de 5.')
    elif numero % 3 == 0:
        print(str(numero) + ' múltiplo de 3.')
    elif numero % 5 == 0:
        print(str(numero) + ' múltiplo de 5.')
    else:
        print(str(numero) + ' nenhum dos dois')