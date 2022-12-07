from math import sqrt
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
#Principio matematico que para formar triangulo cada segmento tem que ser menor que a soma dos outros 2
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
   print('As tres retas formam um triangulo')
else:
    print('As retas não formam triangulo')