nome = str(input('Qual o seu nome? '))
if nome == 'Ivon':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro' or nome == 'João':
    print('Seu nome é bem popular.')
elif nome in 'Deise Veronica Diana Rafaela':
    print('Que belo nome feminino!')
else:
    print('Que nome normal')
print('Bom dia {}{}{}'.format('\033[31m',nome, '\033[m'))