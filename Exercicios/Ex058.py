from random import randint
'''num = 0
ran = ''
pal = 0
while num != ran:
    num = int(input('Digite um numero de 0 a 10: '))
    ran = randint(0, 10)
    pal+=1
    print('Você digitou \033[31m{}\033[m e o computador pensou \033[31m{}\033[m'.format(num, ran))
print('Parabéns!!Finalmente você acertou em \033[34m{}\033[m palpites!!!'.format(pal))
'''
comp = randint(0,10)
print('Pensei em um  numero entre 0 e 10')
acertou = False
palp = 0
while not acertou:
    jog = int(input('Qual o seu palpite? '))
    palp +=1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('Mais...Tente novamente')
        elif comp< jog:
            print('Menos...Tente novamente')
print('Acertou com {} palpites'.format(palp))
