
for c in range(1,6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        n1 = peso
    elif c == 2:
        n2 = peso
    elif c == 3:
        n3 = peso
    elif c == 4:
        n4 = peso
    elif c == 5:
        n5 = peso
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    maior = n1
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    maior = n2
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    maior = n3
elif n4 > n1 and n4 > n2 and n4 > n3 and n4> n5:
    maior = n4
elif n5 > n1 and n5 > n2 and n5 > n3 and n5> n4:
    maior = n5
print('O maior peso é {}'.format(maior))
if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
    menor = n1
elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    menor = n2
elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    menor = n3
elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    menor = n4
elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
    menor = n5
print('O menor peso é {}'.format(menor))
