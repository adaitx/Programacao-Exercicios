numero = int(input('Digite um número: '))

for contador in range(1,11):
    resultado = numero * contador
    print(str(numero) + ' x ' + str(contador) + ' = ' + str(resultado))