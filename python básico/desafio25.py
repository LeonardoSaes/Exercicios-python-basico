# jogo de adivinha
from random import randint
from time import sleep
cores = {'limpa':' \003[m',
         'azul':' \033[1;34m',
         'vermelho':' \033[1;31m',
         'lilas':' \033[1;35m',
         'verde':' \033[1;32m'}

# faz o computador "pensar"
n = randint(0, 5)
print('-' * 55)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 55)
# Jogador tenta adivinhar
jogador = int(input(' Adivinhe o número que pensei: '))
print('{}PROCESSANDO...'.format(cores['azul']))
sleep(2)
if jogador == n:
    print('{}PARABÉNS, VOCÊ ACERTOU!! '.format(cores['verde']))
else:
    print('{}HAHAHA EU GANHEI!! PENSEI NO NÚMERO{}{}{}{}, E NÃO NO{}{}'.format(cores['vermelho'], cores['lilas'], n, cores['lilas'], cores['vermelho'], cores['lilas'], jogador))

