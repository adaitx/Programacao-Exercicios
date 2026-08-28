nome = input('Qual o seu nome? ')
salario = float(input('E qual o seu salário? '))
aumento = float(input('Qual o percentual de aumento que você deseja? '))
salario_novo = salario + (salario*aumento)/100
print ('Muito bem! O seu nome é ' + nome + ' e o seu novo salário é de R$' + str(salario_novo) + '.' )