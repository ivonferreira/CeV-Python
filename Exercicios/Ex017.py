from math import sqrt, hypot
a = float(input('Qual o tamanho do cateto oposto? '))
b = float(input('Qual o tamanho do cateto adjacente? '))
#h = sqrt(a**2+b**2)
print('Com os catetos de {} e {} o valor da hipotenusa é {:.2f}'.format(a, b, sqrt(a**2+b**2)))
print('Com os catetos de {} e {} o valor da hipotenusa é {:.2f}'.format(a, b, ((a**2+b**2)**(1/2))))
print('Com os catetos de {} e {} o valor da hipotenusa é {:.2f}'.format(a, b, (hypot(a,b))))