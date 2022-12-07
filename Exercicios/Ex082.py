lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if op in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
          par.append(v)
    elif v % 2 ==1:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'Os números pares são {par}')
print(f'Os números impares são {impar}')