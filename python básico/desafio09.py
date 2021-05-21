# calcula um desconto de 5% no valor do produto
n = float(input('Digite o valor do produto R$'))
desconto = (n * 5 / 100)
produto = n - desconto
print('O produto que custava R${:.2f},na promoção com desconto de 5% agora custará R${:.2f} '.format(n, produto))


