cid = str(input('Qual sua cidade?' )).strip()
#print('A Cidade tem Santo no nome?{}'.format('Santo'in cid))
print('A cidade tem Santo no nome? {}'.format(cid[:5].upper() == 'SANTO'))