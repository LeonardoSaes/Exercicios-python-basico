# alistamento militar
from datetime import date
print('-' * 40)
print('{}{:^40}'.format('\033[1;31m', 'ALISTAMENTO' '\033[m'))
print('-' * 40)
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu no ano {} completa {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
        saldo = 18 - idade
        print('Faltam {} anos para o alistamento!'.format(saldo))
        ano = saldo + atual
        print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
        print('Realizar o alistamento imediato!')
elif idade > 18:
        saldo = idade - 18
        print('Já deveria ter se alistado há {} anos!'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
