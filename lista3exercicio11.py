numero = int(input('Digite um número inteiro maior que 1: '))

while numero <= 1:
    print('Número inválido!')
    numero = int(input('Digite um número inteiro maior que 1: '))

divisor = 2
primo = True

while divisor < numero:
    if numero % divisor == 0:
        primo = False
        break
    divisor = divisor + 1

if primo:
    print('O número é primo!')
else:
    print('O número não é primo!')