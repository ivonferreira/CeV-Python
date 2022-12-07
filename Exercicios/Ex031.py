km = int(input('Quantos quilometros é sua viagem? '))
#if km <= 200:
#    print('O valor da sua viagem será R${:.2f}'.format(km*0.5))
#else:
#    print('O valor da sua viagem será R${:.2f}'.format(km*0.45))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print('O valor da tarifa da sua viagem é R${:.2f}'.format(preco))
