# verifica se o número é par ou ímpar
n = int(input('Digite um número qualquer: '))
if n % 2 == 0:
    print('O número {} é {}par{}!'.format(n, '\033[1;34m', '\033[m'))
else:
    print('O número {} é {}ímpar{}!'.format(n, '\033[1;31m', '\033[m'))

