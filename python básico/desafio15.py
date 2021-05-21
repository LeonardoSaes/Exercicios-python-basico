# calcula seno, cosseno e tangente de um ângulo
from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {}º tem o Seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {}º tem o Cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {}º tem a Tangente de {:.2f}'.format(angulo, tangente))


