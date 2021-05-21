# lê o primeiro número de uma progressão aritmética e sua razão, depois mostra os primeiros 10 números dessa PA
print('=' * 51)
print('{:^50}'.format('10 TERMOS DE UMA PA'))
print('=' * 51)
primeiro = int(input("Digite o 1º termo: "))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end='-> ')
print('FIM')






