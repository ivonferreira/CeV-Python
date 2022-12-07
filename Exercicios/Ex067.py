n = c = p = 0
while True:
    n = int(input('Digite um número(Negativo para encerrar): '))
    if n >= 0:
        for c in range(0,10):
            c+=1
            p=c*n
            print(f'{n:2} x {c:2} = {p:3}')
    else:
        break
print('Valor negativo,Fim do programa')


