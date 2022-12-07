numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
'''While True:
    c = int(input('Digite um número entre 0 e 20: ')
    if c 0 <= c <=20:
        break
    print('Tente novamente', end = '')'''
c = int(input('Digite um número entre 0 e 20: '))
while c < 0 or c > 20:
    c = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Você digitou o número {numero[c]}')
