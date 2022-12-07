def metade(n,f=False,s='R$'):
    m = n/2
    if f:
        return f'{s}{m:.2f}'.replace('.',',')
    return m
    #return m if f is False else moeda(m)

def dobro(n,f=False,s='R$'):
    d = n*2
    if f:
        return f'{s}{d:.2f}'.replace('.',',')
    return d


def aumentar(n,p,f=False,s='R$'):
    a=(n*p/100)+n
    if f:
        return f'{s}{a:.2f}'.replace('.',',')
    return a


def diminuir(n,p, f=False,s='R$'):
    di = n-(n*p/100)
    if f:
        return f'{s}{di:.2f}'.replace('.',',')
    return di


def moeda(n=0,moeda='R$'):
     return f'{moeda}{n:.2f}'.replace('.',',')


def resumo(n=0,n1=10,n2=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:\t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço:\t{metade(n,True)}')
    print(f'{n1}% de aumento: \t{aumentar(n,n1,True)}')
    print(f'{n2:2}% de redução: \t{diminuir(n,n2, True)}')
    print('-'*30)