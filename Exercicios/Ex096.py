def area(a,b):
    area = a*b
    print(f'A área de um terreno de {a}m por {b}m é {area}m2')


#programa principal
print('Controle de terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)