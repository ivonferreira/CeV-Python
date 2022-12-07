temp = list ()
pessoas = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1]> maior:
            maior = temp[1]
        if temp[1]< menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if r in 'Nn':
        break
print('-='*30)
print(f'Os dados foram {pessoas}')
print(f'Ao todos, você cadastrou {len(pessoas)}')
print(f'O maior peso foi de {maior}Kg', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end =' ')
print(f'\nO maior peso foi de {menor}Kg', end =' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end =' ')