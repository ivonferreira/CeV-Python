n = 0
cont = ''
s = 0
med = 0
maior = 0
menor = 0
c = 1
while c!='END':
    c+=1
    n = int(input('Digite um número '))
    cont = str(input('Deseja continuar?(S/N) ')).upper()
    if cont =='S':
        c+= 1
        s+=n
        med = s/c
        if maior > n:
            maior = n
        elif maior < n:
            maior += 0
        elif menor < n:
            menor = n
        elif menor > n:
            menor +=0
    elif cont == 'N':
        c='END'
    elif cont !='N' or cont !='S':
        print('Digite opção válida')
        c+= 0
print('A soma dos termos é {} e a média {:.2f}'.format(s,med))
print('O maior termo é {} e o menor é {}'.format(maior, menor))