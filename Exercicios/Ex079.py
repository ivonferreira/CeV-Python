lista = []
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não vou adicionar')
    op = str(input('Deseja continuar:[S/N]')).strip().upper()[0]
    if op in 'Nn':
        break
lista.sort()
print(f'Os valores adicionádos são:{lista}')







'''op = ''
while True:
    n = int(input('Digite um número: ')))
    print('Valor adicionado com sucesso!!')
    op = str(input('Deseja continuar[S/N]')).strip().upper()[0]
    if op in 'Nn':
        break
    if index.lista() =
print(lista)
n = 0
c = 1
lista.append(int(input(f'Digite um valor na posição {n}:')))
print('Adicionado no final da lista')
for c in range(1,5):
    n = int(input(f'Digite um número na posição {c}'))
    c+=1
    if n in lista:
        print('Número repetido, não vou adicionar')
    elif n not in lista:
        lista.insert()'''