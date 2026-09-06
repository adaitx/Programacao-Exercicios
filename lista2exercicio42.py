nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite o número de faltas do aluno: '))

if faltas > 15:
    print('Reprovado por falta.')
elif nota >= 9:
    print('Conceito A. ')
elif nota >= 7:
    print('Conceito B. ')
elif nota >= 5:
    print('Conceito C. ')
elif nota < 5:
    print('Conceito D. ')