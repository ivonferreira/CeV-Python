from random import randint
from time import sleep
jogos = list()
print('Valores sorteados:')
maior = 0
tabela = dict()
lista = list()
for j in range(0,4):
    jogos.append(randint(1,6))
    sleep(0.5)
    print(f'O Jogador {j + 1} tirou o número {jogos[j]}')
for k,v in enumerate(jogos):
    tabela['jogo'] = v
    tabela['jogador'] = f'jogador{k+1}'
    lista.append(tabela.copy())
    print(tabela)
    if k==0 and v >maior:
        maior = v
print('Ranking dos jogadores:')
print(f'1º lugar: {lista[0]["jogador"]} com {lista[0]["jogo"]}')
sleep(0.5)
print(f'2º lugar: {lista[1]["jogador"]} com {lista[1]["jogo"]}')
sleep(0.5)
print(f'3º lugar: {lista[2]["jogador"]} com {lista[2]["jogo"]}')
sleep(0.5)
print(f'4º lugar: {lista[3]["jogador"]} com {lista[3]["jogo"]}')
sleep(0.5)