p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
t = p
print('{}'.format(p), end=' ')
while c <=10:
    t= t+r
    print('{}'.format(t), end=' ')
    c+=1
print('Fim')