# calcula seu Indíce Massa Corporea(IMC)
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO!')
elif imc <= 18.5 or imc < 25:
    print('PARABÉNS, VOCÊ ESTÁ NO PESO IDEAL!')
elif imc <= 25 or imc < 30:
    print('VOCÊ ESTÁ EM SOBREPESO!')
elif imc <= 30 or imc <= 40:
    print('VOCÊ ESTÁ COM OBESIDADE!')
else:
    print('VOCÊ ESTÁ COM OBESIDADE MÓRBIDA, CUIDADO!')
