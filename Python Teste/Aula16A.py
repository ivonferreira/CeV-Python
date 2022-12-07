lanche = ('Hamburguer','Suco','Pizza','Pudim', 'Batata Frita') #podemos começar uma variavel composta com ()[] e {} ou até mesmo sem nada
print(lanche[1:3])
print(lanche[-1])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche)
print(sorted(lanche))# em ordem alfabética ou numérica
print(f'São {len(lanche)} lanches')
#lanche[1]= 'Bolo' dá erro pois são imutáveis
#for comida in lanche:
#    print(f'Vou lanchar {comida}') as duas maneira dão o mesmo resultado
#for pos, comida in enumerate(lanche):
#    print(f'Vou lanchar {comida} na posição {pos}') as duas maneira dão o mesmo resultado com a posição
for cont in range(0,(len(lanche))):
    print(f'Vou lanchar {lanche[cont]} na posição {cont}')
print('Comi demais')
