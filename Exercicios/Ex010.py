c = float(input('Quanto você tem na carteira? R$'))
d = c / 5.23
e = c / 5.37
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(c, d, e))
