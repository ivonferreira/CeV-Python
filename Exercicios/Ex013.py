sal = float(input('Qual o valor do seu salário? R$'))
por = float(input('Qual a porcentagem de aumento? '))
#aum = sal*(por*0.01)
aum = sal*por/100
fin = sal+aum
print('Seu salário anterior era de R${:.2f} com um aumento de R${:.2f}\nvocê receberá R${:.2f}'.format(sal, aum, fin))
