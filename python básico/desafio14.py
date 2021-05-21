# calcula o cateto oposto, cateto adjacente e hipotenusa

from math import hypot
n1 = float(input('Digite o cateto oposto: '))
n2 = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(n1, n2)
print('A medida da hipotenusa é {:.2f}'.format(hipotenusa))

# n1 = float(input('Digite o cateto oposto: '))
# n2 = float(input('Digite o cateto adjacente: '))
# hipotenusa = (n1**2 + n2**2) ** (1/2)
# print('A hipotenusa do cateto {} e {} é {:.2f}'.format(n1, n2, hipotenusa))
