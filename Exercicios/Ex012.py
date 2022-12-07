p = float(input('Qual o valor original do produto? R$'))
pct = float(input('Qual a porcentagem de desconto? '))
#d = p*(pct*0.01)
d = p*pct/100
f = p-d
print('O valor do produto era R${:.02f} e com um desconto de {}%,o valor final será R${:.02f}'.format(p, pct, f))