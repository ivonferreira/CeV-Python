frase = input('Digite um frase:').strip().upper()
fraseco = frase.replace(' ','')
letras = len(fraseco)//2
#print(letras)
#print(fraseco[:(letras)-1:-1])
#print(fraseco[:(letras)])
if fraseco[:letras] == fraseco[:letras:-1]:
    print('A frase {} é um \033[34mPALÍNDROMO\033[m'.format(frase))
elif fraseco[:letras] == fraseco[:letras-1:-1]:
    print('A frase {} é um \033[34mPALÍNDROMO\033[m'.format(frase))
else:
    print('A frase {} \033[31mNÃO\033[m é um \033[34mPALÍNDROMO\033[m'.format(frase))
