# Estatísticas em produtos
print('-' * 40)
print('{:^40}'.format('LOJA SUPER BARATO'))
print('-' * 40)
soma = 0
contpreco = 0
cont = 0
menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    soma += preco
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        contpreco += 1
    if resposta == "N":
        break
print('-' * 40)
print('{:-^40}'.format('Fim do programa'))
print('-' * 40)
print(f'O total da compra deu R${soma:.2f} ')
print(f'Temos {contpreco} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor}')


