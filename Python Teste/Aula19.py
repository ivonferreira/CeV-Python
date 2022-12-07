pessoas = {'nome': 'Gustavo','sexo':'M','idade':'22'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
for k,v in pessoas.items():
    print(k,v)
del pessoas['sexo']
print(pessoas)
pessoas['nome'] = 'Ivon'
print(pessoas)