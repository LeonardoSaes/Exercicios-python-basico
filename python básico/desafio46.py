# soma todos os valores q são ímpares, multiplos de 3 e q estão entre 1 e 500
soma = 0
contador = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        contador += 1
print('A soma de todos os {} valores é {}'.format(contador, soma))




