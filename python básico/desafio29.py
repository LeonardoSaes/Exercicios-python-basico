# verifica dse o ano é bissexto
from datetime import date
ano = int(input('Que ano deseja analisar? Digite 0 para analisar ano atual: '))
if ano == 0:
    ano = date.today().year
# ano bissexto é divisível por 4, por 400 e anos divisíveis por 100 ñ são
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))

else:
    print('{} não é um ano bissexto!'.format(ano))

