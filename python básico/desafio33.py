# empréstimo bancário
from time import sleep
print('-' * 40)
print('        {}EMPRESTIMO BANCÁRIO{}'.format('\033[1;34m', '\033[m'))
print('-' * 40)
casa = float(input('Digite o valor da casa:R$ '))
salario = float(input('Digite o seu salário:R$ '))
salario30 = (salario * 30) / 100
anos = int(input('Digite em quantos anos deseja parcelar: '))
print('{}PROCESSANDO...{}'.format('\033[1;33m', '\033[m'))
sleep(2)
prestacao = casa / (anos * 12)
if prestacao <= salario30:
    print('{}Seu parcelamento foi aprovado!{}'.format('\033[1;32m', '\033[m'))
    print('Valor da parcela: {}R${:.2f}{}'.format('\033[1;35m', prestacao, '\033[m'))

else:
    print('{}Sinto muito, mas o senhor(a) não poderá parcelar a casa.{}'.format('\033[1;31m', '\033[m'))
    print('{}Valor da parcela: R${:.2f}, excede 30% do seu salário.{}'.format('\033[1;31m', prestacao, '\033[m'))
