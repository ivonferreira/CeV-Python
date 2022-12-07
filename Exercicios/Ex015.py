tempo = int(input('Quantos dias você Alugou o Carro? '))
km = float(input('Quantos Km você rodou? '))
#vt=tempo*60
#vk=km*0.15
pago = (tempo*60)+(km*0.15)
#print('O valor a ser pago é R${:.2f}'.format(vt+vk))
print('O valor a ser pago é R${:.2f}'.format(pago))