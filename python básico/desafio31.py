# calcula os aumentos de acordo com o salário
salario = float(input('Digite seu salária atual:R$ '))
if salario <= 1250:
    aumento = salario + (salario * 15) / 100
    print('-' * 50)
    print('Parabéns, você ganhou um aumento de {}15%{}.'.format('\033[4;32m', '\033[m'))
    print('Salário atual:{}R${:.2f}{}'.format('\033[4;32m', aumento, '\033[m'))
    print('-' * 50)
else:
    aumento = salario + (salario * 10) / 100
    print('-' * 50)
    print('Parabéns, você ganhou um aumento de {}10%{}.'.format('\033[4;32m', '\033[m'))
    print('Salário atual:{}R${:.2f}{}'.format('\033[4;32m', aumento, '\033[m'))
    print('-' * 50)

