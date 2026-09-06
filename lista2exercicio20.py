a = int(input('Digite o valor do primeiro lado do triângulo: '))
b = int(input('Digite o valor do segundo lado do triângulo: '))
c = int(input('Digite o valor do terceiro lado do triângulo: '))

print((a + b) > c and (a + c) > b and (b + c) > a)