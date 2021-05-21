# calcula um aumento de 15% do salário digitado
salario = float(input('Digite o seu salária atual R$'))
aumento = (salario * 15) / 100
satual = salario + aumento
print('Um funcionário que ganhava R${:.2f}, com o aumento de 15% passa a receber R${:.2f}  '.format(salario, satual))

