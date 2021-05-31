# cadastro de pessoas
resposta = "".upper()
contidade = 0
conthomem = 0
contmulher = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRO DE PESSOAS'))
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    if resposta == 'N':
        break
print('-' * 30)
print(f'Ao todo foram cadastradas {contidade} pessoas com mais de 18 anos')
print(f'Total de homens cadastrados: {conthomem}')
print(f'E temos {contmulher} mulheres com menos de 20 anos.')
