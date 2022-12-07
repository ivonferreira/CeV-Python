sal = int(input('Qual o seu salário? R$'))
#sals = sal+(sal*0.10)
#sali = sal+(sal*0.15)
if sal <= 1250:
    aum = sal*0.15
else:
    aum = sal*0.10
print('Quem ganhava R${:.2f} o novo salário é de R${:.2f}'.format(sal, (sal+aum)))