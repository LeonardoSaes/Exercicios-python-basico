# Lê 5 valores e verifica qual o maior e o menor
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}º pessoa:(Kg) '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso lido {}Kg'.format(maior))
print('Menor peso lido {}Kg'.format(menor))

