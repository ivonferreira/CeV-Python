'''op = 0
while op != 5:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print('Selecione a operação:
    [ 1 ] Soma
    [ 2 ] Multiplicação
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair')
    op = int(input('Qual sua opção: '))
    if op == 1:
        res = num1+num2
        print('{:2} + {:2} = {:3}'.format(num1, num2, res))
    elif op == 2:
        res = num1*num2
        print('{:2} X {:2} = {:3}'.format(num1, num2, res))
    elif op ==3:
        if num1 > num2:
            maior = num1
            print('O maior é {}'.format(maior))
        elif num2 > num1:
            maior = num2
            print('O maior é {}'.format(maior))
        else:
            print('{} e {} são iguais'.format(num1,num2))
    elif op == 4:
        op = 0
    elif op < 1 or op > 5:
        print('Digite uma opção correta')
    else:
        print('FIM')'''
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op =0
res = 0
while op!=5:
    print('''[ 1 ] Somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair''')
    op = int(input('Qual é a opção? '))
    if op ==1:
        soma = n1+n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    elif op ==2:
        prod = n1*n2
        print('O produto entre {} e {} é {}'.format(n1,n2,prod))
    elif op ==3:
        if n1 >n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1,n2,maior))
    elif op ==4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro numero:'))
        n2 = int(input('Segundo numero: '))
    elif op ==5:
        print('Saindo...')
    else:
        print('Opção invalida')
    sleep(2)
print('Fim do programa')
