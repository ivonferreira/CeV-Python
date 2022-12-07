n = int(input('Digite um número inteiro: '))
print('Escolha uma Operação:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
op = int(input('Qual sua opção?:'))
lim = int(input('Escolha até onde vai a tabuada:'))
if op == 1:
    for c in range(0,lim+1):
        s = c+n
        print('{:2} \033[31m+\033[m {:2} = {:3}'.format(c,n,s))
elif op == 2:
    for c in range(0,lim+1):
        s = c-n
        print('{:2} \033[31m-\033[m {:2} = {:3}'.format(c,n,s))
elif op ==3:
    for c in range(0,lim+1):
        s = c*n
        print('{:2} \033[31mX\033[m {:2} = {:3}'.format(c,n,s))
elif op ==4:
    for c in range(0,lim+1):
        s = c/n
        print('{:2} \033[31m÷\033[m {:2} = {:3}'.format(c,n,s))
else:
    print('Digite uma opção válida')