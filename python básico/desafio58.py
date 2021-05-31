# calcula o fatorial de um número utilizando while
numero = int(input('Fatorial de: '))
cont = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    fatorial *= cont
    cont -= 1
    if cont > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print('{}'.format(fatorial))

