# soma todos os números pares digitados
soma = 0
contador = 0
for c in range(1, 7):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('A soma entre os {} números PARES digitados foi {}'.format(contador, soma))





