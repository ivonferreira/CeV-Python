n = s = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    if n==999:
        break
    s+=n
    c+=1
print('A soma de %c números é %s' % (c,s))#Python 2
print('A soma de {} números é {}'.format(c,s))#Python 3
print(f'A soma de {c} números é {s}')#Python 3.6+
#Nova forma de escrever as variaveis no print no lugar do format