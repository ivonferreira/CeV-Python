def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a +b
    print(f'A soma de A + B = {s}')
def soma2(* valores):
    s = 0
    for num in valores:
        s+= num
    print(f'Somando os valores {valores} temos {s}')

#programa principal
soma(1, 2)
soma(a=8, b=5)
soma(b=9, a=6)
soma2(7,8,9,0,1)