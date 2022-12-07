valor = float(input('Qual o valor do ben? R$'))
sal = float(input('Qual o seu salário mensal? R$'))
anos = int(input('Quantos anos será o prazo? '))
pres = valor/(anos*12)
print('Para um bem no valor de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, pres))
if pres <= sal*0.30:
    print('O emprestimo foi {}{}{}'.format('\033[32m','APROVADO','\033[m'))
else:
    print('O emprestimo foi \033[31mNEGADO\033[m')