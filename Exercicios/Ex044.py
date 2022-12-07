preco = float(input('Qual o valor do produto? R$'))
print('-=-'*12)
print('Qual será a forma de pagamento?\n1 - À vista no dinheiro\n2 - À vista no cartão ou debito\n3 - 2 vezes sem Juros no cartão\n4 - 3 vezes ou mais no cartão')
print('=-='*12)
pag = int(input('Escolha sua opção: '))
if pag == 1:
    precof = preco - (preco*0.1)
    forma = '\033[32mDINHEIRO\033[m'
elif pag == 2:
    precof = preco - (preco*0.05)
    forma = '\033[34mDEBITO\033[m'
elif pag == 3:
    precof = preco
    forma = '\033[36mCREDITO\033[m'
elif pag == 4:
    precof = preco + (preco*0.2)
    forma = '\033[31nPARCELADO\033[m'
else:
    print('Escolha uma opção válida')
print('A forma de pagamento escolhida foi {} e o valor a ser pago será R${:.2f}'.format(forma, precof))
