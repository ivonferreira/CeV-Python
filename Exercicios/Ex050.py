s = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n%2 == 0:
        s= s + n
        cont += 1
    else:
        s+=0
print('A soma dos {} numeros pares é \033[31m{}\033[m'.format(cont,s))