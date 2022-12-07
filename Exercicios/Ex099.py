from time import sleep
def maior(valores):
    if valores == list():
        maior = 0
    print('Analisando os valores passados...')
    for i,v in enumerate(valores):
        if i == 0 or maior < v:
            maior = v
        print(f'{v} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('-='*30)

#programa principal
lista1 = [2,9,4,5,7,1]
lista2 = [4,7,0]
lista3 = [1,2]
lista4 = [6]
lista5 = list()
maior(lista1)
maior(lista2)
maior(lista3)
maior(lista4)
maior(lista5)