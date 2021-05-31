# progressão aritmética melhorada utilizando while
print('=-' * 10)
print('{:^17}'.format('GERADOR DE PA'))
print('=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos'.format(total))
print('FIM')