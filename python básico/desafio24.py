# mostra seu primeiro e último nome
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('-' * 60)
print('Muito prazer em te conhecer, {}{}{}'.format('\033[1;34m', nome, '\033[m'))
print('Seu primeiro nome é {}{}{}'.format('\033[1;33m', n[0], '\033[m'))
print('Seu último nome é {}{}{}'.format('\033[1;31m', n[len(n)-1], '\033[m'))
print('-' * 60)

