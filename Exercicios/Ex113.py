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

def leiaFloat(msg):
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

#programa principal
n1 = leiaint('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O numero inteiro digitado é {n1} e o real é {n2}')
