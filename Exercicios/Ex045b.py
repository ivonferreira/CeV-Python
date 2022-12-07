from random import randint
print('JOKENPÔ SHELDON COOPER')
print('='*20)
print('Escolha seu simbolo:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Lagarto\n5 - Spock')
print('='*20)
jog = int(input('Escolha sua opção:'))
pc = randint(1,5)
if jog == 1 and pc == 3:
    jogs = '\033[37mPEDRA\033[m'
    pcs = '\033[34mTESOURA\033[m'
    fim = 'Venceu'
elif jog == 1 and pc == 2:
    jogs ='\033[37mPEDRA\033[m'
    pcs = '\033[33mPAPEL\033[m'
    fim = 'Perdeu'
elif jog == 1 and pc == 1:
    jogs = '\033[37mPEDRA\033[m'
    pcs = '\033[37mPEDRA\033[m'
    fim = 'Empatou'
elif jog == 1 and pc == 4:
    jogs = '\033[37mPEDRA\033[m'
    pcs = '\033[32mLAGARTO\033[m'
    fim = 'Venceu'
elif jog == 1 and pc == 5:
    jogs = '\033[37mPEDRA\033[m'
    pcs = '\033[36mSPOCK\033[m'
    fim = 'Perdeu'
elif jog == 2 and pc == 1:
    jogs ='\033[33mPAPEL\033[m'
    pcs = '\033[37mPEDRA\033[m'
    fim = 'Venceu'
elif jog == 2 and pc == 2:
    jogs ='\033[33mPAPEL\033[m'
    pcs = '\033[33mPAPEL\033[m'
    fim = 'Empatou'
elif jog == 2 and pc == 3:
    jogs = '\033[33mPAPEL\033[m'
    pcs = '\033[34mTESOURA\033[m'
    fim = 'Perdeu'
elif jog == 2 and pc == 4:
    jogs = '\033[33mPAPEL\033[m'
    pcs = '\033[32mLAGARTO\033[m'
    fim = 'Perdeu'
elif jog == 2 and pc == 5:
    jogs = '\033[33mPAPEL\033[m'
    pcs = '\033[36mSPOCK\033[m'
    fim = 'Venceu'
elif jog == 3 and pc == 1:
    jogs = '\033[34mTESOURA\033[m'
    pcs = '\033[37mPEDRA\033[m'
    fim = 'Perdeu'
elif jog == 3 and pc == 2:
    jogs = '\033[34mTESOURA\033[m'
    pcs ='\033[33mPAPEL\033[m'
    fim = 'Venceu'
elif jog == 3 and pc == 3:
    jogs = '\033[34mTESOURA\033[m'
    pcs = '\033[34mTESOURA\033[m'
    fim = 'Empatou'
elif jog == 3 and pc ==4:
    jogs = '\033[34mTESOURA\033[m'
    pcs = '\033[32mLAGARTO\033[m'
    fim = 'Venceu'
elif jog == 3 and pc == 5:
    jogs = '\033[34mTESOURA\033[m'
    pcs = '\033[36mSPOCK\033[m'
    fim = 'Perdeu'
elif jog == 4 and pc == 1:
    jogs = '\033[32mLAGARTO\033[m'
    pcs = '\033[37mPEDRA\033[m'
    fim = 'Perdeu'
elif jog == 4 and pc == 2:
    jogs = '\033[32mLAGARTO\033[m'
    pcs = '\033[33mPAPEL\033[m'
    fim = 'Venceu'
elif jog == 4 and pc == 3:
    jogs = '\033[32mLAGARTO\033[m'
    pcs = '\033[34mTESOURA\033[m'
    fim = 'Perdeu'
elif jog == 4 and pc == 4:
    jogs = '\033[32mLAGARTO\033[m'
    pcs = '\033[32mLAGARTO\033[m'
    fim = 'Empatou'
elif jog == 4 and pc == 5:
    jogs = '\033[32mLAGARTO\033[m'
    pcs = '\033[36mSPOCK\033[m'
    fim = 'Venceu'
elif jog == 5 and pc == 1:
    jogs = '\033[36mSPOCK\033[m'
    pcs = '\033[37mPEDRA\033[m'
    fim = 'Venceu'
elif jog == 5 and pc == 2:
    jogs = '\033[36mSPOCK\033[m'
    pcs = '\033[33mPAPEL\033[m'
    fim = 'Perdeu'
elif jog == 5 and pc == 3:
    jogs = '\033[36mSPOCK\033[m'
    pcs = '\033[34mTESOURA\033[m'
    fim = 'Venceu'
elif jog == 5 and pc == 4:
    jogs = '\033[36mSPOCK\033[m'
    pcs = '\033[32mLAGARTO\033[m'
    fim = 'Perdeu'
elif jog ==5 and pc ==5:
    jogs = '\033[36mSPOCK\033[m'
    pcs = '\033[36mSPOCK\033[m'
    fim = 'Empatou'
else:
    print('\033[41mVocê não escolheu uma opção válida!!!\033[m')
print('Você escolheu {} e o computador {}, sendo assim você {}'.format(jogs, pcs, fim))
