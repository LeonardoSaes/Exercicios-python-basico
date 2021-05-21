# calcula o preço da viagem
n = float(input('Digite a distância da viagem em Km: '))
if n <= 200:
    print('A viagem de {}Km custará R${:.2f}'.format(n, n * 0.5))
else:
    print('A viagem de {}Km custará R${:.2f}'.format(n, n * 0.45))
