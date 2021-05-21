# verifica se o número digitado é um número primo ou não
numero = int(input('Digite um número inteiro: '))
mult = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        mult += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes,'.format(numero, mult))
if mult == 2:
    print('portanto, ele É PRIMO.')
else:
    print('por isso, ele NÃO É PRIMO.')
