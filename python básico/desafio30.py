primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
terceiro = int(input('Terceiro número: '))

# achando o maior número
maior = primeiro
if segundo < primeiro:
    maior = segundo
if terceiro > maior:
    maior = terceiro

# achando o menor número
menor = primeiro
if segundo < primeiro:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print('Menor número: {}{}{}'.format('\033[1;31m', menor, '\033[m'))
print('Maior número: {}{}{}'.format('\033[1;36m', maior, '\033[m'))
