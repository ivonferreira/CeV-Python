a= 0
cont = 0
for c in range(1,501,2):
    if c%3 ==0:
        cont = cont + 1
        a+=c
#       a = a + c
#       cont+= 1
print('O Somatório dos {} numeros multiplos impares de 3 até 500 é:{}'.format(cont, a))
