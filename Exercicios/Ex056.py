somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('-------- {}ª PESSOA ---------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20+=1
mediaidade = somaidade/4
print('A media da idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velhos se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menor de 20 anos'.format(totmulher20))
