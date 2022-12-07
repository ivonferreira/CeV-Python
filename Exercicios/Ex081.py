lista=[]
op = ''
#c = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    c += 1
    op = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if op in 'Nn':
        break
    elif op not in 'SsNn':
        print('Opção incorreta')
print(f'Foram digitados {len(lista)} números')
#print(f'Foram digitados {c} números')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é : {lista}')
if 5 in lista:
    print('O Valor 5 está na lista')
else:
    print('O valor 5 não está na lista')