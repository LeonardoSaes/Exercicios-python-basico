# mostra seu nome em maiusculo, minusculo, quantidade de letras total e do 1º nome
nome = input('Digite o seu nome completo: ')
maiusculo = nome.upper()
minusculo = nome.lower()
letras = len(nome.replace(' ', ''))
nprimeiro = nome.split()
letrasq = len(nprimeiro[0])
print('-' * 40)
print('Nome em maiúsculo: {}\nNome em minúsculo: {} '.format(maiusculo, minusculo))
print('Quantidade de letras: {}\nQuantidade de letras do primeiro nome: {}'.format(letras, letrasq))
print('-' * 40)



