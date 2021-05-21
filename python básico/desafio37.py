# calcula a média do aluno e fala se foi aprovado ou reprovado
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5:
    print('{}REPROVADO!{}'.format('\033[1;31m', '\033[m'))
elif media == 5 or media <= 6.9:
    print('{}RECUPERAÇÃO!{}'.format('\033[1;33m', '\033[m'))
else:
    print('{}APROVADO!{}'.format('\033[1;32m', '\033[m'))
