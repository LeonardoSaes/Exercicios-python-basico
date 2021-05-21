# calcula a sua categoria de acordo com seu ano de nascença
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
categoria = ano_atual - ano
if categoria <= 9:
    print('VOCÊ tem {} anos.'.format(categoria))
    print('ATÉ 9 ANOS:{}CATEGORIA MIRIM{}'.format('\033[4;35m', '\033[m'))
elif categoria <= 14:
    print('VOCÊ TEM {} ANOS.'.format(categoria))
    print('ATÉ 14 ANOS:{}CATEGORIA INFANTIL{}'.format('\033[4;36m', '\033[m'))
elif categoria <= 19:
    print('VOCÊ TEM {} ANOS.'.format(categoria))
    print('ATÉ 19 ANOS:{}CATEGORIA JUNIOR{}'.format('\033[4;32m', '\033[m'))
elif categoria <= 25:
    print('VOCÊ TEM {} ANOS.'.format(categoria))
    print('ATÉ 25 ANOS:{}CATEGORIA SÊNIOR{}'.format('\033[4;33m', '\033[m'))
else:
    print('VOCÊ TEM {} ANOS.'.format(categoria))
    print('ACIMA DE 20:{}CATEGORIA MASTER{}'.format('\033[4;34m', '\033[m'))
