# caixa eletrônico
print('=' * 54)
print('{:^50}'.format('LOJAS SAES'))
print('=' * 54)
preco = float(input('digite o total da compra: R$'))
print('-' * 54)
print('{}DIGITE 1 PARA{}: À VISTA DINHEIRO/CHEQUE: 10% DESCONTO'.format('\033[1;31m', '\033[m'))
print('{}DIGITE 2 PARA{}: À VISTA NO CARTÃO: 5% DESCONTO'.format('\033[1;32m', '\033[m'))
print('{}DIGITE 3 PARA{}:EM ATÉ 2X NO CARTÃO: PREÇO NORMAL'.format('\033[1;33m', '\033[m'))
print('{}DIGITE 4 PARA{}: EM 3X OU MAIS NO CARTÃO: 20% DE JUROS'.format('\033[1;34m', '\033[m'))
print('-' * 54)
pagamento = float(input('Digite a forma de pagamento: '))
if pagamento == 1:
    desconto1 = (preco * 10) / 100
    desconto = preco - desconto1
    print('Valor da compra: R${:.2f}'.format(preco))
    print('Produto será pago a vista no dinheiro,desconto de R${}'.format(desconto1))
    print('Valor final:{}R${:.2f}{}'.format('\033[1;32m', desconto, '\033[m'))
elif pagamento == 2:
    desconto = (preco * 5) / 100
    total = preco - desconto
    print('Valor da compra: R${:.2f}'.format(preco))
    print('Produto será pago a vista no cartão,desconto de R${}'.format(desconto))
    print('Valor final:{}R${:.2f}{}'.format('\033[1;32m', total, '\033[m'))
elif pagamento == 3:
    print('Valor da compra: R${:.2f}'.format(preco))
    print('Produto será pago em até 2x no cartão, preço normal R${}'.format(preco))
    print('Valor final:{}R${:.2f}{}'.format('\033[1;32m', preco, '\033[m'))
elif pagamento == 4:
    parcelas = int(input('Quantas Parcelas? '))
    juros = (preco * 20) / 100
    compra = preco + juros
    total = compra / parcelas
    print('Valor da compra: R${:.2f}'.format(preco))
    print('Produto será pago em {}x de R${},com juros de R${}'.format(parcelas, total, juros))
    print('Valor final:{}R${:.2f}{}'.format('\033[1;32m', compra, '\033[m'))
else:
    compra = preco
    print('{}OPÇÃO INVÁLIDA, TENTE NOVAMENTE.{}'.format('\033[1;31m', '\033[m'))
    print('Valor final:{}R${:.2f}{}'.format('\033[1;32m', preco, '\033[m'))
