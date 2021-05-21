# PEDRA, PAPEL OU TESOURA
from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''ESCOLHA SUA JOGADA: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Digite sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
print('-' * 30)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-' * 30)
if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('DEU EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('DEU EMPATE')
    elif jogador == 2: # COMPUTADOR JOGOU TESOURA
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('DEU EMPATE')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('JOGADA INVÁLIDA')
