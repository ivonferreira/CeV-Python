def contador(*num):
    for valor in num:
        print(f' {valor} ',end='')
    print(f'Recebi os valores {num} e tem {len(num)} elementos')

#programa principal
contador(2, 1, 7)
contador(9,0)
contador(1,5,4,7,6)