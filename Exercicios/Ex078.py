lista = []
maior = menor = 0
for n in range(0,5):
    lista.append(int(input(f'Digite um número na posição {n}: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n]> maior:
            maior = lista [n]
        if lista[n]< menor:
            menor = lista [n]

print(f'Você digitou os valores:{lista}')
print(f'O maior valor é {maior} que está nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f' {i}', end='')
print()
print(f'O menor valor é {menor} que está nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f' {i}', end='')