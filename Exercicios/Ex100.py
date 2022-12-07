from random import randint
from time import sleep
def sorteia(lista):
    print(f'Sorteando os 5 valores da lista ', end='')
    while len(lista) != 5:
        num = (randint(1,10))
        lista.append(num)
        print(f'{num} ', end='')
        sleep(0.3)
    print('PRONTO!')
def somaPar(lista):
    s = 0
    for c in lista:
        if c % 2 ==0:
            s += c
    print(f'Somando os valores pares de {lista}, temos {s}')


#programa principal
numeros= list()
sorteia(numeros)
somaPar(numeros)