valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')
print('\n')
for c,v in enumerate(valores):
    print(f'Na posição {c} temos o valor {v}!')
print('Fim da lista')