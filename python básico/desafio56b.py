# jogo do adivinha utilizando while
from random import randint
computador = randint(0, 10)
print('-' * 42)
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
print('-' * 42)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tenta de novo ')
            print('-' * 42)
        elif jogador > computador:
            print('Menos...Tenta de novo ')
            print('-' * 42)
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
