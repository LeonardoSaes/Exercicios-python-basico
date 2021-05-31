# Lê vários números, informa a média entre todos,
# a quantidade de números digitados,
# o maior e o menor e
# a soma entre todos os valores
soma = 0
media = 0
cont = 0
maior = 0
menor = 0
resposta = 'S'
while resposta in 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
