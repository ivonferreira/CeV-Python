a = [8,9,3,4,5]
#b = a    dessa forma cria-se uma ligação entre as duas listas e se modificar uma a outra tb muda
b = a[:] # Assim fazemos com que b receba os elementos dentro da lista a, criando uma copia independente
b[2] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')