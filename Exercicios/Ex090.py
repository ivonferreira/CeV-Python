boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média de {boletim["nome"]} :'))
if boletim['media'] >= 7:
    boletim['sit'] = 'Aprovado'
elif boletim['media'] >=5:
    boletim['sit'] = 'Em Recuperação'
else:
    boletim['sit'] = 'Reprovado'
print('-='*10)
for k,v in boletim.items():
    print(f'{k} é igual a {v}')
