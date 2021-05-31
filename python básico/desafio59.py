# progressão aritmética utilizando while
print('=-' * 10)
print('{:^17}'.format('GERADOR DE PA'))
print('=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
