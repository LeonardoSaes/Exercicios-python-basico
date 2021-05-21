# calcula o valor do aluguel considerando dias alugados e Km percorridos
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km percoridos? '))
calculo = (dias * 60) + (km * 0.15)
print('-' * 65)
print('Dias alugados {}, Km percorridos {}, total a pagar: R${:.2f}'.format(dias, km, calculo))
print('-' * 65)


