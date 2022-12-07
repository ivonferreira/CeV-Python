'''n = 1
while n!=0:
    sexo = str(input('Qual o seu sexo? ')).strip()[0]
    if sexo in 'Mm':
        print('Seu sexo é Masculino')
        n = 0
    elif sexo in 'Ff':
        print('Seu sexo é Feminino')
        n = 0
    else:
        print('Digite uma opção válida')
print('FIM')'''
#alternativa
sexo = str(input('Qual o seu sexo? ')).strip()[0]
while sexo not in 'MmFf':
    sexo=str(input('Opção inválida. Qual o seu sexo?' )).strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))