n_secreto = 33
numero = int(input('Tente adivinhar o número secreto: '))

while numero != n_secreto:
    if numero > n_secreto:
        print()
        print('O palpite foi maior! ')
    elif numero < n_secreto:
        print()
        print('O palpite foi menor! ')
        
    numero = int(input('Tente novamente: '))
print()
print('Você acertou o número! Parabéns!')