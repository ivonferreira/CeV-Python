from random import randint
a = randint(1,10)
b = randint(1,10)
c = randint(1,10)
d = randint(1,10)
e = randint(1,10)
num = (a,b,c,d,e)
#numo = sorted(num)
print(f'Os valores sorteados são:{num}')
#print(f'O menor número é {numo[0]}')
#print(f'O maior número é {numo[4]}')
print(f'O maior valor sorteado é {max(num)}')
print(f'O menor valor sorteado é {min(num)}')