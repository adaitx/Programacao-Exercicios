criancas = 0
adolescentes = 0
adultos = 0
idosos = 0

idade = int(input('Digite uma idade (0 para encerrar): '))

while idade != 0:
    if idade < 12:
        criancas = criancas + 1
    else:
        if idade < 18:
            adolescentes = adolescentes + 1
        else:
            if idade < 60:
                adultos = adultos + 1
            else:
                idosos = idosos + 1

    idade = int(input('Digite uma idade (0 para encerrar): '))

print()
print('Quantidade de crianças:', criancas)
print('Quantidade de adolescentes:', adolescentes)
print('Quantidade de adultos:', adultos)
print('Quantidade de idosos:', idosos)