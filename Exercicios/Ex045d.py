from random import randint
from time import sleep
print('-=-'*16)
print('{:^46}'.format('JO KEN PO SHELDON COOPER'))
print('-=-'*16)
itens = ('Pedra', 'Papel', 'Tesoura','Lagato','Spock')
pc = randint(0,4)
print('''Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
[ 3 ] LAGARTO
[ 4 ] SPOCK''')
jog = int(input('Qual é a sua jogada? '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
print('LAGARTO')
sleep(1)
print('SPOCK!!!!!')
print('-*-'*10)
print('O computador escolheu {}'.format(itens[pc]))
print('O jogador escolheu {}'.format(itens[jog]))
print('-*-'*10)
if pc == 0:
    if jog ==0:
        print('Empate')
    elif jog ==1:
        print('Jogador Vence')
    elif jog ==2:
        print('Computador Vence')
    elif jog ==3:
        print('Computador Vence')
    elif jog ==4:
        print('Jogador Vence')
    else:
        print('Escolha uma opção válida')
elif pc == 1:
    if jog ==0:
        print('Computador Vence')
    elif jog ==1:
        print('Empate')
    elif jog ==2:
        print('Jogador Vence')
    elif jog == 3:
        print('Jogador Vence')
    elif jog == 4:
        print('Computador Vence')
    else:
        print('Escolha uma opção válida')
elif pc == 2:
    if jog ==0:
        print('Jogador Vence')
    elif jog ==1:
        print('Computador Vence')
    elif jog ==2:
        print('Empate')
    elif jog == 3:
        print('Computador Vence')
    elif jog == 4:
        print('Jogador Vence')
    else:
        print('Escolha uma opção válida')
elif pc == 3:
    if jog ==0:
        print('Jogador Vence')
    elif jog ==1:
        print('Computador Vence')
    elif jog ==2:
        print('Jogador Vence')
    elif jog ==3:
        print('Empate')
    elif jog ==4:
        print('Computador Vence')
    else:
        print('Escolha uma opção válida')
elif pc == 4:
    if jog == 0:
        print('Computador Vence')
    elif jog == 1:
        print('Jogador Vence')
    elif jog == 2:
        print('Computador Vence')
    elif jog == 3:
        print('Jogador Vence')
    elif jog == 4:
        print('Empate')
    else:
        print('Escolha uma opção válida')
