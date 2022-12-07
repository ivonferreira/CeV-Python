jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
gols = list()
totgols = 0
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(0,partidas):
    gols.append(int(input(f'   Quantos gols na partida {g}? ')))
#    totgols+=gols[g]
    totgols = sum(gols)
jogador['gols'] = gols[:]
jogador['total'] = totgols
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
#print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for k,v in enumerate(gols):
    print(f'    => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {totgols} gols.')