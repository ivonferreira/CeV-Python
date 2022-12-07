lista = ('Pão', 1.00, 'Manteiga', 3.00, 'Leite', 7.00, 'Sal', 0.75, 'Farinha', 4.00, 'Ovos', 1.2,'Condensado', 5.00,'Chocolate', 7.00)
print('*'*40)
print('{:^40}'.format('Lista de Compras'))
print('*'*40)
for pos in range(0,len(lista)):
    if pos %2 ==0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('*'*40)