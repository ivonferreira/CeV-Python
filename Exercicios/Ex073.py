camp = ('Palmeiras','Flamengo','Corinthians','Fluminense', 'Atlético Paranaense', 'Internacional','Atlético Mineiro', 'América MG', 'Bragantino','Santos','São Paulo', 'Botafogo','Goiás', 'Ceará','Fortaleza','Cuiabá','Avaí','Coritiba','Atlético Goianiense','Juventude')
print(f'Os times do brasileirão são:{camp}')
print(f'O 5 primeiros são {camp[:5]}')
print(f'Zona do rebaixamento {camp[-4:]}')
print(f'Em ordem alfabética os times são: {sorted(camp)}')
print('O Avaí está na {}ª posição'.format(camp.index('Avaí')+1))