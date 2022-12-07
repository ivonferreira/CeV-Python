def ajuda(msg):
        print(f'\033[7:40m{msg.__doc__}')
def esclin(txt):
    print(f'\033[46m~' * (len(txt)+4))
    print(f'  {txt}')
    print(f'~' * (len(txt)+4))
#programa principal
while True:
    print(f'\033[0;42m~' * 30)
    print('    SISTEMA DE AJUDA PyHELP')
    print(f'~' * 30)
    e = str(input(f'\033[mFunção ou Biblioteca >'))
    if e.upper == 'FIM':
        print(f'\033[41m~'*15)
        print('   ATÉ LOGO!')
        print('~'*15)
        print(f'\033[m')
        break
    esclin(f'Acessando o manual do comando {e}')
    ajuda(e)
