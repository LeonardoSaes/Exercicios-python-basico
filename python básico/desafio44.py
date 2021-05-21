# contagem regressiva de 10 até 0 esperando 1 segundo
from time import sleep
import emoji
print('-' * 20)
print('CONTAGEM REGRESSIVA')
print('-' * 20)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BOOMM!!:boom:', use_aliases=True))

