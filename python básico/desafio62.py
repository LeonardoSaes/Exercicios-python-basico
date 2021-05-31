# Lê vários números, mostra quantos foram digitados e
# soma todos
numero = 0
soma = 0
cont = 0
numero = int(input('Digite um número [999 pra parar]: '))
while True:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 pra parar]: '))
    if numero == 999:
        break
print('Você digitou {} números, a soma entre todos é {}'.format(cont, soma))
