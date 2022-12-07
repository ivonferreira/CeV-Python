total = caro1000 = barato = cont= 0
nomeb = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    cont+=1
    total += preco
    if preco > 1000:
        caro1000+=1
    if cont == 1 or preco < barato:
        barato = preco
        nomeb = nome
    op =' '
    while op not in 'SN':
        op = str(input('Deseja Continuar?[S/N]:')).strip().upper()[0]
    if op == 'N':
        break
print(f'O total da compra foi: R${total:.2f}')
print(f'Temos {caro1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi: {nomeb} e custou: R${barato:.2f}')