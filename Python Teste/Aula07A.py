n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
sb = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
r = n1%n2
print('A soma vale {}, a subtração {}, \n a multiplicação {}, a divisão {:.2f}'.format(s, sb, m, d), end='')
print(', o valor de {} elevado a {} é igual a {}'.format(n1, n2, e),end='')
print(' e a divisão de {} por {} fica {} restando {}'.format(n1, n2, di, r))
