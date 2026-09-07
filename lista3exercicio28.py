print('Tabela de conversão (°C para °F)')

for celsius in range(0,101,10):
    fahrenheit = celsius * 9/5 + 32
    print((str(celsius) + '°C = ' + str(fahrenheit) + '°F'))