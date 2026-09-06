idade = int(input('Digite a idade do usuário: '))

if idade < 12:
    print('Faixa etária: criança. ')
elif idade < 18:
    print('Faixa etária: adolescente. ')
elif idade < 60:
    print('Faixa etária: adulto. ')
else:
    print('Faixa etária: idoso. ')