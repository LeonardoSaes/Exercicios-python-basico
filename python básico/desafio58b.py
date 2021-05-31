# calcula o fatorial de um número utilizando for
resultado = 1
numero = int(input('Fatorial de: '))
for c in range(1, numero + 1):
    resultado *= c
print('O fatorial de {} é {}'.format(numero, resultado))
