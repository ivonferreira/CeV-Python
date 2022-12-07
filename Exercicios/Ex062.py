p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
t = p
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while c <= tot:
        print('{}'.format(t), end=' ')
        t= t+r
        c+=1
    print('PAUSA')
    mais = int(input('Quer adicionar mais quantos termos? '))
print('Progressão finalizada com {} termos'.format(tot))