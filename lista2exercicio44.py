idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo (M ou F): ')

if sexo == 'M':

    if idade >= 18:
        print('Apto ao serviço militar!')
    else:
        print('Menor de idade.')
elif sexo == 'F':
    print('Mulheres não precisam servir militarmente.')
else:
    print('Categoria inválida.')