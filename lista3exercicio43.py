for contador in range(1,11):
    nota = float(input('Digite a ' + str(contador) + 'ª nota: '))
    
    if nota >= 9:
        print('Conceito A.')
    elif nota >= 7:
        print('Conceito B.')
    elif nota >= 5:
        print('Conceito C.')
    else:
        print('Conceito D.')

print()