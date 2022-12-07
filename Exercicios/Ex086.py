matriz = list()
linha1 = list()
linha2 = list()
linha3 = list()
for c0 in range(0, 3):
    linha1.append(int(input(f'Digite um valor para [0,{c0}]: ')))
for c1 in range(0, 3):
    linha2.append(int(input(f'Digite um valor para [1,{c1}]: ')))
for c2 in range(0, 3):
    linha3.append(int(input(f'Digite um valor para [2,{c2}]: ')))
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)
print('-=-'*7)
print(f'[ {matriz[0][0]:2} ] [ {matriz[0][1]:2} ] [ {matriz[0][2]:2} ]')
print(f'[ {matriz[1][0]:2} ] [ {matriz[1][1]:2} ] [ {matriz[1][2]:2} ]')
print(f'[ {matriz[2][0]:2} ] [ {matriz[2][1]:2} ] [ {matriz[2][2]:2} ]')
print('-=-'*7)