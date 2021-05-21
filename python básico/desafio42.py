# PEDRA, PAPEL OU TESOURA
from random import choice
from time import sleep
print('-' * 33)
print('{}{:^32}{}'.format('\033[1;34m', 'JOKENPÔ', '\033[m'))
print('-' * 33)
n1 = str(input('{}PEDRA, PAPEL OU TESOURA?{} '.format('\033[1;36m', '\033[m'))).upper()
lista = ['PEDRA', 'PAPEL', 'TESOURA']

# sorteia um elemento da lista
sorteio = choice(lista)
print('{}PROCESSANDO...{}'.format('\033[1;35m', '\033[m'))
sleep(2)
# todas as possibilidades
if n1 == 'PEDRA' and sorteio == 'PAPEL':
    print('-' * 33)
    print('COMPUTADOR JOGOU PAPEL')
    print('VOCÊ JOGOU PEDRA')
    print('-' * 33)
    print('{}COMPUTADOR VENCEU{}'.format('\033[1;31m', '\033[m'))
elif n1 == 'PEDRA' and sorteio == 'TESOURA':
    print('-' * 33)
    print('COMPUTADOR JOGOU TESOURA')
    print('VOCÊ JOGOU PEDRA')
    print('-' * 33)
    print('{}VOCÊ VENCEU{}'.format('\033[1;32m', '\033[m'))
elif n1 == 'PEDRA' and sorteio == 'PEDRA':
    print('-' * 33)
    print('COMPUTADOR JOGOU PEDRA')
    print('VOCÊ JOGOU PEDRA')
    print('-' * 33)
    print('{}DEU EMPATE{}'.format('\033[1;33m', '\033[m'))
elif n1 == 'PAPEL' and sorteio == 'PEDRA':
    print('-' * 33)
    print('COMPUTADOR JOGOU PEDRA')
    print('VOCÊ JOGOU PAPEL')
    print('-' * 33)
    print('{}VOCÊ VENCEU{}'.format('\033[1;32m', '\033[1m'))
elif n1 == 'PAPEL' and sorteio == 'TESOURA':
    print('-' * 33)
    print('COMPUTADOR JOGOU TESOURA')
    print('VOCÊ JOGOU PAPEL')
    print('-' * 33)
    print('{}COMPUTADOR VENCEU{}'.format('\033[1;31m', '\033[m'))
elif n1 == 'PAPEL' and sorteio == 'PAPEL':
    print('-' * 33)
    print('COMPUTADOR JOGOU PAPEL')
    print('VOCÊ JOGOU PAPEL')
    print('-' * 33)
    print('{}DEU EMPATE{}'.format('\033[1;33m', '\033[m'))
elif n1 == 'TESOURA' and sorteio == 'PAPEL':
    print('-' * 33)
    print('COMPUTADOR JOGOU TESOURA')
    print('VOCÊ JOGOU PEDRA')
    print('-' * 33)
    print('{}VOCÊ VENCEU{}'.format('\033[1;32m', '\033[m'))
elif n1 == 'TESOURA' and sorteio == 'PEDRA':
    print('-' * 33)
    print('COMPUTADOR JOGOU PEDRA')
    print('VOCÊ JOGOU TESOURA')
    print('-' * 33)
    print('{}COMPUTADOR VENCEU{}'.format('\033[1;31m', '\033[m'))
elif n1 == 'TESOURA' and sorteio == 'TESOURA':
    print('-' * 33)
    print('COMPUTADOR JOGOU TESOURA')
    print('VOCÊ JOGOU TESOURA')
    print('-' * 33)
    print('{}DEU EMPATE{}'.format('\033[1;33m', '\033[m'))
else:
    print('{}OPÇÃO INVÁLIDA{}'.format('\033[1;31m', '\033[m'))

