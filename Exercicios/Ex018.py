from math import sin, cos, tan, radians
n = int(input('Qual o angulo em Graus: '))
#o seno cosseno e tangente precisa que o numero
#seja convertido em radianos para isso usamos
#o radians
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print('Do angulo {}º o seno é {:.2f}, o cosseno é {:.2f} e tangente {:.2f}'.format(n, s, c, t))

