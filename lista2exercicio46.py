n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

frequencia = int(input('Digite a frequência do aluno (em %): '))

if frequencia >= 75:
    if (n1+n2)/2 >= 6:
        print('Aprovado.')
    else:
        print('Reprovado por nota.')
else:
    print('Reprovado por falta.')