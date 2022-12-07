from datetime import date
ano = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, date.today().year))
if idade > 19:
    print('Já passou seu tempo de se alistar em {}{}{} anos'.format('\033[34m',(idade-18),'\033[m'))
elif idade == 19:
    print('Já passou seu tempo de se alistar em {}{}{} ano'.format('\033[34m', (idade - 18), '\033[m'))
elif idade == 18:
    print('É hora de se {}ALISTAR{} você já tem {} anos'.format('\033[7;33m','\033[m',idade))
elif idade == 17:
    print('Falta {}{}{} ano para você se apresentar'.format('\033[31m', (18 - idade), '\033[m'))
else:
    print('Faltam {}{}{} anos para você se apresentar'.format('\033[31m', (18-idade), '\033[m'))
print('O ano de alistamento: {}'.format(ano+18))

