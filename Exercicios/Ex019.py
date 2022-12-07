from random import choice
a1 = input('Qual o nome do primeiro aluno(a)? ')
a2 = input('Qual o nome do segundo aluno(a)? ')
a3 = input('Qual o nome do terceiro aluno(a)? ')
a4 = input('Qual o nome do quarto aluno(a)?')
lista = [a1, a2, a3, a4]
#escolhido = choice(lista)
print('O aluno que apagara o quadro será {}'.format(choice(lista)))

