'''num = int(input('Digite um número a ser fatorado: '))
r = -1
m = 1
c = 1
while num != 1:
    num = num -1
    m = m*(num+1)
    print('{} X '.format(num+1), end='')
print('1 = {}'.format(m))'''
'''from math import factorial
num = int(input('Digite um número a ser fatorado: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num,f))'''
num = int(input('Digite um número a ser fatorado: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x 'if c>1 else' = ', end=' ')
    f*=c
    c-= 1
print('{}'.format(f))