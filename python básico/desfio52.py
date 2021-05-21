# verifica a idade de 7 pessoas e mostra quantas são maiores de idade e menores
from datetime import date
contador = 0
contador2 = 0
ano_atual = date.today().year
for c in range(1, 8):
    nascenca = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = ano_atual - nascenca
    if idade < 18:
        contador += 1
    else:
        contador2 += 1
print('Entre todas as pessoas, {} são maiores de idade,'.format(contador2))
print('E {} são menores de idade'.format(contador))

