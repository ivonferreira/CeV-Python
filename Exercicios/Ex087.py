matriz = list()
linha1 = list()
linha2 = list()
linha3 = list()
par = maior = soma3 = 0
for c0 in range(0, 3):
    linha1.append(int(input(f'Digite um valor para [0,{c0}]: ')))
    if linha1[c0] % 2 == 0:
        par += linha1[c0]
for c1 in range(0, 3):
    linha2.append(int(input(f'Digite um valor para [1,{c1}]: ')))
    if linha2[c1] % 2 == 0:
        par+=linha2[c1]
    if c1 == 0:
        maior = linha2[c1]
    else:
        if linha2[c1] > maior:
            maior = linha2[c1]

for c2 in range(0, 3):
    linha3.append(int(input(f'Digite um valor para [2,{c2}]: ')))
    if linha3[c2] % 2 == 0:
        par+=linha3[c2]
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)
soma3 = matriz[0][2]+matriz[1][2]+matriz[2][2]
print('-+-'*7)
print(f'[ {matriz[0][0]:2} ] [ {matriz[0][1]:2} ] [ {matriz[0][2]:2} ]')
print(f'[ {matriz[1][0]:2} ] [ {matriz[1][1]:2} ] [ {matriz[1][2]:2} ]')
print(f'[ {matriz[2][0]:2} ] [ {matriz[2][1]:2} ] [ {matriz[2][2]:2} ]')
print('-+-'*7)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')