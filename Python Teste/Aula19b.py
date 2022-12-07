'''brasil = []
estado1 = {'uf':'Pernambuco','sigla':'PE'}
estado2 = {'uf':'Alagoas','sigla':'AL'}
brasil.append(estado1)
brasil.append(estado1)

print(brasil[0]['sigla'])'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] =str(input('Sigla do Estado: ')).strip().upper()[:2]
    brasil.append(estado.copy()) #funciona como o [:] nos dicionários
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
