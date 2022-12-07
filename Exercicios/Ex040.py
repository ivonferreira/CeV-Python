n1 = float(input('Qual a nota da primeira prova? '))
n2 = float(input('Qual a nota da segunda prova? '))
med = (n1+n2)/2
print('Sua média foi {:.1f}'.format(med))
if med < 5.0:
    sit = '\033[7;41mREPROVADO\033[m'
elif 6.9 >= med >= 5.0:
#elif med >=5.0 and med <=6.90:
    sit = '\033[7;43mEM RECUPERAÇÃO\033[m'
else:
    sit = '\033[7:44mAPROVADO\033[m'
print('Sua situação é: {}'.format(sit))
