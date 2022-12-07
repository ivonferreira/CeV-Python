def leiaDinheiro(msg):
    valido = False
    while not valido:
        i = str(input(msg)).replace(',','.').strip()
        if i.isalpha() or i == '':
            print(f'\033[31mERRO!\"{i}\" não é preço válido\033[m')
        else:
            valido = True
            return float(i)