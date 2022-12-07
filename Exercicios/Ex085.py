lista = list()
par = list()
impar = list()
p=0
for p in range(1,8):
    n = int(input(f'Digite {p}º número: '))
    if n%2 ==0:
        par.append(n)
        par.sort()
    else:
        impar.append(n)
        impar.sort()
lista.append(par[:])
lista.append(impar[:])
print('-=-'*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
