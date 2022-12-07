alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura da parede? '))
a = alt*lar
t = a/2
print('A area da parede de {} x {} é {:.1f} e você precisará de {:.01f} Litros de tinta para pinta-la'.format(alt, lar, a, t))