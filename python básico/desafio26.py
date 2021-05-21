# radar rodoviário
km = float(input('Digite a velocidade do carro: '))
if km > 80:
    print('{}Você será multado por estar {}Km/h acima do permitido!'.format('\033[1;31m', km - 80))
    print('Sua multa será no valor de R${}{}'.format('\033[4m', (km - 80) * 7))
else:
    print('{}Você está dirigindo dentro do limite, continue assim!'.format('\033[1;32m'))
