# calcula quantos livros prrecisará para pintar uma parede
largura = float(input('Digite a largura da sua parede em metros: '))
altura = float(input('Digite a altura da sua parede em metros: '))
area = largura * altura
litros = area / 2
print('A área da sua parede mede {} m² e precisará de {} litros para pinta-la '.format(area, litros))
