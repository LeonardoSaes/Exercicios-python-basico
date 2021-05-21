# converte qualquer coisa para binário, octal ou hexadecimal
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE.')
