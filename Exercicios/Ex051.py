n = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão da Progressão? '))
for c in range(n,n+(r*10),r):
    print(c, end=',')

