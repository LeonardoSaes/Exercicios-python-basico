# tabuada de vários números utilizando while
tabuada = 0
cont = 0
numero = int(input('Quer ver a tabuada de qual número? '))
print('-' * 35)
while True:
    print(f'{numero} x {tabuada} = {numero * tabuada}')
    tabuada += 1
    if tabuada > 10:
        tabuada = 0
        print('-' * 35)
        numero = int(input('Quer ver a tabuada de qual número? '))
        print('-' * 35)
    if numero < 0:
        break
print('TABUADA ENCERRADA, VOLTE SEMPRE!')


