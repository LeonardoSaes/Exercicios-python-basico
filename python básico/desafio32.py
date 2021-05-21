# verifica se os segmentos podem formar um triângulo
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos {}PODEM{} formar um triângulo!'.format('\033[1;34m', '\033[m'))
else:
    print('Esses segmentos {}NÃO{} podem formar um triângulo'.format('\033[1;31m', '\033[m'))
