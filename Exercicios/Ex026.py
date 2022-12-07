frase = str(input('Escreva uma frase: ')).strip().upper()
print('A frase tem {} letras "a"'.format(frase.count('A')))
print('A primeira vez que a letra aparece é a {}ª posição'.format(frase.find('A')+1))
print('A ultima vez que essa letra aparece é a {}ª posição'.format(frase.rfind('A')+1))
