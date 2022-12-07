n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1>n2:
    print('O Primeiro numero {}{}{} é {}MAIOR{}'.format('\033[33m',n1,'\033[m','\033[7;41m','\033[m'))
elif n1<n2:
    print('O Segundo numero {}{}{} é {}MAIOR{}'.format('\033[34m', n2, '\033[m', '\033[7;44m', '\033[m'))
else:
    print('O numeros são \033[7;45mIGUAIS\033[m')