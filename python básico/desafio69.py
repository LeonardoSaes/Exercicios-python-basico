# Simulador de caixa eletrônico
print('-' * 40)
print('{:^40}'.format('BANCO SAES'))
print('-' * 40)
valor = int(input('Qual o valor que deseja sacar? R$ '))
total = valor
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('-' * 40)
print('''VOLTE SEMPRE AO BANCO SAES 
TENHA UM BOM DIA!''')

