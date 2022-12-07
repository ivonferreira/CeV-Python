s = 0
n = 0
from datetime import date
for c in range(1,8):
    ano = int(input('Qual o ano a {}ª pessoa nasceu?' .format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        s= s + 1
    else:
        n += 1
print('No total são {} maiores e {} são menores de idade'.format(s, n))