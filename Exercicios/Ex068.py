from random import randint
n = pc = s = c = 0
op = ''
while True:
    n = int(input('Digite um número: '))
    pc = randint(0,10)
    s = n + pc
    op = str(input('Qual sua opção [P/I]: ')).strip().upper()[0]
    if op in 'Pp':
        if s % 2 == 0:
            print(f'Você Jogou {n} e o computador {pc}. Total foi {s} PAR')
            print('Você Venceu!Vamos Jogar novamente...')
            c+=1
        else:
            print(f'Você Jogou {n} e o computador {pc}. Total foi {s} IMPAR')
            break
    if op in'Ii':
        if s % 2 == 1:
            print(f'Você Jogou {n} e o computador {pc}. Total foi {s} IMPAR')
            print('Você Venceu!Vamos Jogar novamente...')
            c+=1
        else:
            print(f'Você Jogou {n} e o computador {pc}. Total foi {s} PAR')
            break
print('Você Perdeu!')
print(f'GAME OVER!Foram {c} vitórias.')

