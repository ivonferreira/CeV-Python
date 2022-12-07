from random import randint
from time import sleep
num = int(input('Digite um numero de 0 a 5: '))
ran = randint(0, 5)
print('PROCESSANDO...')
sleep(3)
if num == ran:
    print('Parabéns você acertou, o numero era mesmo {}'.format(num))
else:
    print('Você errou, o numero era {} e voce digitou {}'.format(ran, num))