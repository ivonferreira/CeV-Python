nome = str(input('Qual o seu nome completo? ')).strip()

print('Seu nome em Maiuscula:{}'.format(nome.upper()))
print('Seu nome em minusculo:{}'.format(nome.lower()))
nomes = nome.split()
#nomej = ''.join(nomes)
#print('São {} caracteres sem espaço'.format(len(nomej)))
print('São {} caracteres no seu nome'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome {} tem {} letras'.format(nomes[0],len(nomes[0])))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))