num = int(input('Digite um numero: '))
op = int(input('Selecione a opção:\n1 - Para binário\n2 - Para octal\n3 - hexadecimal\nOpção: '))
if op == 1:
    print('O numero digitado em binário é {}{}{}'.format('\033[34m',bin(num)[2:],'\033[m'))
elif op == 2:
    print('O numero digitado em octal é {}{}{}'.format('\033[32m',oct(num)[2:],'\033[m'))
elif op == 3:
    print('O numero digitado em Hexadecimal é {}{}{}'.format('\033[33m',hex(num)[2:],'\033[m'))
else:
    print('Digite uma opção válida!')
#os colchetes com o numero é para fatiar e tirar os dois primeiros digitos que so serve para simbolizar o formato(0b binario,0o octal e 0x hexa)