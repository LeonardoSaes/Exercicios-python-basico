# jogo do par ou ímpar
from random import randint
print('-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-' * 30)
contvitoria = 0
while True:
    numero = int(input('Diga um valor de 0 a 10: '))
    tipo = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = numero + computador
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    print('-' * 30)
    print(f'Você jogou {numero} e o computador {computador}.')
    print(f'Total de {soma}')
    print('DEU PAR 'if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU')
            print('Tente novamente...')
            print('-' * 30)
            contvitoria += 1
        else:
            print('VOCÊ PERDEU')
            print('GAME OVER')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU')
            print('Tente novamente...')
            print('-' * 30)
            contvitoria += 1
        else:
            print('VOCÊ PERDEU')
            print('GAME OVER')
            break
print(f'Você venceu {contvitoria} vezes')


