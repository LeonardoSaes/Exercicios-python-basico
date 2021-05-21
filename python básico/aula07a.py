nome = str(input('Qual é o seu nome? '))
print('Prazer em te conhecer {}'.format(nome))
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
di = n1 / n2
mul = n1 * n2
sub = n1 - n2
print('A soma dos números são {}, a divisão é {}, a multiplicação é {} e '.format(s, di, mul), end='')
print('a subtração é {}'.format(sub))
