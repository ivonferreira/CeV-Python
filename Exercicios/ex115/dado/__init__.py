c = ('\033[m',           # 0 = sem cor
    '\033[0;31m',        # 1 = vermelho
    '\033[0;32m',        # 2 = verde
    '\033[0;33m',        # 3 = amarelo
    '\033[0;34m',        # 4 = azul
    '\033[0;35m',        # 5 = roxo
    '\033[7;30m'         # 6 = preto
     );


def leiadinheiro(msg):
    valido = False
    while not valido:
        i = str(input(msg)).replace(',','.').strip()
        if i.isalpha() or i == '':
            print(f'\033[31mERRO!\"{i}\" não é preço válido\033[m')
        else:
            valido = True
            return float(i)


def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError,TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31m\nEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return a


def leiafloat(msg):
    while True:
        try:
            a = float(input(msg))
        except (ValueError,TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31m\nEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return a


def titulo(msg, cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('-' * tam)
    print(f'{msg}'.center(tam))
    print('-' * tam)
    print(c[0], end='')

def titmenu(msg, cor=0):
    print(c[cor], end='')
    print('-' * 50)
    print(f'{msg}'.center(50))
    print('-' * 50)
    print(c[0], end='')

def opmenu(n,msg,cor=4):
    print(f'{c[3]}{n} - {c[cor]}{msg}{c[0]}')
