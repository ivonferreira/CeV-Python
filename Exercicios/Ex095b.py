time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for g in range(0,partidas):
        gols.append(int(input(f'   Quantos gols na partida {g}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if resp in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N')
    if resp in 'Nn':
        break
print('-='*30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostra dados de qual jogador?[999 para sair]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'  ==LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('Volte Sempre!!')
