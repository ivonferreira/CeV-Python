pessoas = dict()
lista = list()
mulheres = list()
grupo = media = somaid = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    grupo+=1
    somaid += pessoas['idade']
    if pessoas['sexo'] in 'MmFf':
        mulheres.append(pessoas['nome'][:])
    op = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if op in 'Nn':
        break
media = somaid/len(pessoas)
print(f'O grupo tem {grupo} pessoas')
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas são: {mulheres}')
for c in pessoas['idade']:
    if c > media:
        print(pessoas)