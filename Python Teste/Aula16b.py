a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a
print(c)
print(len(c))
print(c.count(5))# conta quantos numeros 5 tem
print(c.index(5))# em que posição está o numero 5 na primeira ocorrencia
print(c.index(5,2))# em que posição está o numero 5 a partir da posição 2
print(d)
pessoa = ('Ivon', 36, 'M',117.50)# as tuplas podem ter vários tipos de dados
print(pessoa)
#del(pessoa) A tupla só pode ser apagada
#del(pessoa[1]) Não pode apagar um elemento só
#print(pessoa)