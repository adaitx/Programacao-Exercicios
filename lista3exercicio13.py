soma = 0
contador = 0

while True:
    nota = float(input('Digite a nota do aluno (Digite -1 para sair): '))
    if nota == -1:
        break
    else:
        soma = soma + nota
        contador = contador + 1

if contador > 0:
    media = soma / contador
    print('A média das notas é ' + str(media) + '.')
else:
    print('Nenhuma nota foi digitada.')