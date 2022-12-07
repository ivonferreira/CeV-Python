p=1
op = sexo =''
cont18 = hom = mul20 = 0
while True:
    idade = int(input(f'Qual a idade da {p}ª pessoa:'))
    sexo = str(input(f'Qual o sexo da {p}ª pessoa:[M/F]:')).strip().upper()[0]
    p+=1
    op = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if op in 'Ss':
        print(f'REGISTRADO: Idade:{idade}, sexo: {sexo}')
        if idade >18:
            cont18+=1
        if sexo == "M":
            hom+=1
        if sexo == 'F' and idade <=19:
            mul20+=1
        if sexo not in 'MmFf':
            sexo = str(input(f'Qual o sexo da {p}ª pessoa:[M/F]:')).strip().upper()[0]
    elif op in 'Nn':
        print(f'REGISTRADO: Idade:{idade}, sexo: {sexo}')
        if idade > 18:
            cont18 += 1
        if sexo == "M":
            hom += 1
        if sexo == 'F' and idade <= 19:
            mul20 += 1
        if sexo not in 'MmFf':
            sexo = str(input(f'Qual o sexo da {p}ª pessoa:[M/F]:')).strip().upper()[0]
        break
    else:
        op = str(input('Quer continuar: [S/N]')).strip().upper()[0]
print(f'Foram {cont18} pessoas com mais que 18 anos, {hom} homens e {mul20} mulheres com menos de 20')