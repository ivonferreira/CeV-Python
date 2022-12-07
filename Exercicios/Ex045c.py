from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('''Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!')
if pc == 0:
    if jog ==0:
        print('Empate')
    elif jog ==1:
        print('Jogador Vence')
    elif jog ==2:
        print('Computador Vence')
    else:
        print('Escolha uma opção válida')
elif pc == 1:
    if jog ==0:
        print('Computador Vence')
    elif jog ==1:
        print('Empate')
    elif jog ==2:
        print('Jogador Vence')
    else:
        print('Escolha uma opção válida')
elif pc == 2:
    if jog ==0:
        print('Jogador Vence')
    elif jog ==1:
        print('Computador Vence')
    elif jog ==2:
        print('Empate')
    else:
        print('Escolha uma opção válida')
print('-*-'*10)
print('O computador escolheu {}'.format(itens[pc]))
print('O jogador escolheu {}'.format(itens[jog]))
print('-*-'*10)