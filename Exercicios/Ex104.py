def leiaint(msg):
    print('-'*30)
    while True:
        a = str(input(msg))
        if a.isnumeric():
            break
        print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    return a


#programa principal
n = leiaint('Digite um número: ')
print(f'O número digitado é {n}')