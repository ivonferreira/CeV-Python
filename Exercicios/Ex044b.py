print('{:=^36}'.format('LOJAS IVOX'))
preco = float(input('Qual o valor do produto? R$'))
print('-=-'*12)
print('Qual será a forma de pagamento?\n1 - À vista no dinheiro\n2 - À vista no cartão ou debito\n3 - 2 vezes sem Juros no cartão\n4 - 3 vezes ou mais no cartão')
print('=-='*12)
pag = int(input('Escolha sua opção: '))
if pag == 1:
    precof = preco - (preco*0.1)
    forma = '\033[32mDINHEIRO\033[m'
    parc = 1
    valp = precof
elif pag == 2:
    precof = preco - (preco*0.05)
    forma = '\033[34mDEBITO\033[m'
    parc = 1
    valp = precof
elif pag == 3:
    precof = preco
    forma = '\033[36mCREDITO\033[m'
    parc = 2
    valp = precof/2
elif pag == 4:
    precof = preco + (preco*0.2)
    forma = '\033[31mPARCELADO\033[m'
    parc = int(input('Quantas Parcelas? :'))
    valp = precof/parc
else:
    print('Escolha uma opção válida')
print('A forma de pagamento escolhida foi {} e o valor a ser pago será R${:.2f}'.format(forma, precof))
print('Você pagará {} parcelas de R${:.2f}'.format(parc, valp))
