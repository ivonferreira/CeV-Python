frase = input('Digite um frase:').strip().upper()
palavras = frase.split()
fraseco = ''.join(palavras)
inverso = fraseco[::-1]
'''for letra in range(len(fraseco)-1,-1,-1):
    inverso += fraseco[letra]'''
print('O inverso de {} é {}'. format(fraseco, inverso))
if inverso == fraseco:
    print('É um PALINDROMO')
else:
    print('Não é um PALINDROMO')
