def fatorial(n,show=False):
    """
    Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-'*30)
    f=1
    for c in range(n,0,-1):
        f *= c
        if show == True:
            if c ==1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} X ', end='')
    return f


#programa principal
print(fatorial(5, True))