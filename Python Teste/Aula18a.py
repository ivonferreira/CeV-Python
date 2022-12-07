'''teste = []
teste.append('Ivon')
teste.append('38')
galera = []
galera.append(teste[:])
teste[0]='Maria'
teste[1] = 22
galera.append(teste)
print(galera)'''
galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria',45]]
print(galera[2][1])
for p in galera:
#    print(p[0])#o nome
#    print(p[1])#a idade
    print(f'{p[0]} tem {p[1]} anos de idade.')

