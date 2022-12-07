a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o quarto número: '))
num = (a, b, c, d)
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na posição : {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram:', end ='')
for n in num:
    if n %2 ==0:
        print(n, end = ' ')