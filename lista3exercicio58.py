soma = 0

for dia in range(7):
    horas = float(input('Digite as horas trabalhadas no dia: '))
    soma = soma + horas

if soma >= 40:
    print('Carga semanal: Pesada')
elif soma >= 20:
    print('Carga semanal: Moderada')
else:
    print('Carga semanal: Leve')