# Lê o nome, idade e sexo de 4 pessoas, mostra o nome e idade do homem mais velho,
# quantas mulheres tem menos de 20 anos e
# a média de idade de todos.
somaidade = 0
mulherestot20 = 0
maioridadehomem = 0
nomevelho = ''
for c in range(1, 5):
    print('-----{}ºPESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherestot20 += 1
mediaidade = somaidade / 4
print('A média de idade de todas as idades é {} anos.'.format(mediaidade))
print('{} mulheres tem menos de 20 anos.'.format(mulherestot20))
print('O homem mais velho tem {} anos e se chama. {}'.format(maioridadehomem, nomevelho))


