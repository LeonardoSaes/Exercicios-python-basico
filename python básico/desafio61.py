# sequência de fibonacci
print('-' * 50)
print('{:^45}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-' * 50)
numero = int(input('Quantos números da sequecia quer ver? '))
t1 = 0
t2 = 1
print('{}->{}'.format(t1, t2), end='')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print('->{}->'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('-' * 50)
