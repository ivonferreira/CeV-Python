jogador = dict()
gols = list()
tabela = list()
while True:
    nome = str(input('Nome do Jogador: '))
    jogador['nome'] = nome
    part = int(input(f'Quantas partidas {nome} jogou? '))
    soma = 0
    for p in range(0,part):
        gol = int(input(f'Quantos gols na partida {p}?'))
        gols.append(gol)
        soma+= gol
        jogador['gols'] = gols[:]
    jogador['total'] = soma
    gols.clear()
    tabela.append(jogador.copy())
    op = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if op in 'Nn':
        break
for c,k in enumerate(tabela):
    print(f'{c} {k["nome"]} {k["gols"]} {k["total"]}')
while True:
    op2 = int(input('Mostrar dados de que jogador: '))
    if op2 == 999:
            print(tabela)
            break
    elif op2 > len(tabela[op2]['gols']):
            print('Opção inválida. Tente novamente')
    elif op2 == tabela[op2]['gols']:
        for j in range(0,len(tabela[op2]['gols'])):
            print(f'No jogo {j} fez {tabela[op2]["gols"][j]} gols')

print('Volte Sempre')


