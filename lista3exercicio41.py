for numero in range(1,11):
    if numero % 2 == 0:
        print()
        print('Tabuada do número ' + str(numero))
        for contador in range (1,11):
            resultado = numero * contador
            print(str(numero) + ' x ' + str(contador) + ' = ' + str(resultado))