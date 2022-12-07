velo = int(input('Qual a velocidade do seu carro? '))
if velo > 80:
    print('Você foi MULTADO em R${:.2f}'.format((velo-80)*7))

print('Bom dia e dirija com segurança')