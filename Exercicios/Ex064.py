n = c = cont = s = 0
'''while c !='end':
    n = int(input('Digite um número: '))
    if n == 999:
        c ='end'
    else:
        cont+=1
        s+=n
print('Foram digitados {} números e a soma deles {}'.format(cont,s))'''
n = int(input('Digite um número [999 para sair]: '))
while n !=999:
    s+=n
    cont+=1
    n= int(input('Digite um número [999 para sair:] '))
print('Você digitou {} números e a soma entre eles é {}'. format(cont,s))