palavras = ('Pegasus', 'Dragao','Fenix','Andromeda','Cisne','Unicornio','Urso','Hidra','Lobo', 'Leao')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end = '')