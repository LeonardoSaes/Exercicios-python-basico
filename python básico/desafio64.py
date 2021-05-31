# Lê vários números, mostra quantos foram digitados e
# a soma entre eles
cont = 0
soma = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    cont += 1
    if numero == 999:
        cont -= 1
        break
    soma += numero
print(f'Foram digitados {cont} números ')
print(f'A soma entre todos foi {soma}')

