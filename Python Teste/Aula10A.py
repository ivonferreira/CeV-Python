'''nome = str(input('Qual o seu nome? '))
if nome =='Ivon':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m <=6.99:
    print('Você está de recuperação, sua media foi {:.2f}'.format(m))
else:
    print('Você passou por média, parabéns sua media foi {:.2f}!'.format(m))
#print('Parabéns' if m >=7 else 'Estude mais')   forma simplificada