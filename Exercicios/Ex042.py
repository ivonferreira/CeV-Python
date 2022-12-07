r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
#    if r1==r2 and r2 == r3:
    if r1==r2==r3:
        tipo = '\033[31mEquilátero\033[m'
    elif r1 == r2 and r1!= r3 or r2 == r3 and r2 != r1 or r3 == r1 and r3 != r2:
        tipo = '\033[32mIsóceles\033[m'
    else:
#   elif r1 != r2 != r3 != r1
        tipo = '\033[33mEscaleno\033[m'
    print('Os três segmentos formam um triângulo {}'.format(tipo))
else:
    print('Os três segmentos não formam um triângulo')