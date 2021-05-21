# verifica se os segmentos formar um triangulo equilátero, escaleno ou isósceles
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos {}PODEM{} formar um triângulo '.format('\033[1;34m', '\033[m'), end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Esses segmentos {}NÃO PODEM{} formar um triângulo!'.format('\033[1;31m', '\033[m'))
