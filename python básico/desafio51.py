# verifica se a frase é um palíndromo, ou seja, a msm coisa de trás pra frente,
# desconsiderando espaços e virgulas
frase = str(input('Digite uma frase: ')).upper().strip()
frase = frase.replace(' ', '')
inverso = frase[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if frase == inverso:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
