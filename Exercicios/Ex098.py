from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*15)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <=f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont+=p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')



#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
p1 = int(input('Inicio: '))
u = int(input('Fim: '))
r = int(input('Passo: '))
contador(p1, u, r)