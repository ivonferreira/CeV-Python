nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Muito prazer em te conhecer {}'.format(lista[0]))
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu ultimo nome é {}'.format(lista[len(lista)-1]))
