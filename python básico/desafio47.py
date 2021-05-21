# tabuada usando estrutura de repetição for

numero = int(input('Digite um número para ver sua tabuada: '))
print('-' * 15)
print('TABUADA DO {}'.format( numero))
print('-' * 15)
for c in range(0, 11):
    print('{} x {} = {}'.format(numero, c, numero * c))
