ingresso = 50

print()
print('Bom dia! Seja bem-vindo ao evento!')

while ingresso > 0:
    pergunta = input('Deseja vender mais um ingresso (S/N)? ')    
    if pergunta == 'S':
        ingresso = ingresso - 1
        print()
        print('Ingresso vendido! ')
        print('O total de ingressos disponíveis é de ' + str(ingresso) + '.')
        print()
    elif pergunta == 'N':
        print()
        print('Agradecemos sua presença! Volte sempre')
        break
    else:
        print()
        print('Opção inválida!')