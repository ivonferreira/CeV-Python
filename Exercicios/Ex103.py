def ficha(a='', b=0):
    print(f'O jogador {a} marcou {b} gol(s) no campeonato')


#Programa Principal
j = str(input('Nome do Jogador: ')).strip().title()
g = str(input('Número de Gols: '))
if j == '':
    j='<desconhecido>'
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(j,g)