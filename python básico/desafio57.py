# menu de opções para escolher o que fazer
from time import sleep
n = 0
while True:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('segundo valor: '))
    print('-' * 30)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior ')
    print('[4] Novos números ')
    print('[5] Sair do programa')
    print('-' * 30)
    resposta = int(input('>>> O que você deseja fazer?'))
    if resposta == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
        print('-' * 30)
    elif resposta == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
        print('-' * 30)
    elif resposta == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior é {}'.format(n1, n2, n1))
            print('-' * 30)
        else:
            print('Entre {} e {}, o maior é {}'.format(n1, n2, n2))
            print('-' * 30)
    elif resposta == 4:
        n = 0
    elif resposta == 5:
        break
    else:
        print('Opção inválida,Tente novamente')
        print('-' * 30)
        resposta = 0
        sleep(2)
print('FIM DO PROGRAMA, VOLTE SEMPRE!')

