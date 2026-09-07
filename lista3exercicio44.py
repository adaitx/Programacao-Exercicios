temperatura = float(input('Digite o valor da temperatura da água (digite qualquer número menor que -100 para interromper o programa): '))

while temperatura >= -100:
    if temperatura >= 30:
        print('Quente.')
        print()
    elif temperatura >= 15:
        print('Agradável.')
        print()
    elif temperatura >= 0:
        print('Fria.')
        print()
    else:
        print('Congelante.')
        print()

    temperatura = float(input('Digite o valor da temperatura da água (digite qualquer número menor que -100 para interromper o programa): '))

print('Programa interrompido.')