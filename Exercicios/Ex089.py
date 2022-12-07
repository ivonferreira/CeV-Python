boletim = list()
aluno = list()
notas = list()
media = list()
while True:
    aluno.append(str(input('Nome: ')))
    for p in range(1,3):
        notas.append(float(input(f'Nota {p}: ')))
    aluno.append(notas[:])
    boletim.append(aluno[:])
    notas.clear()
    aluno.clear()
    op = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if op in 'Nn':
        break
print('-'*30)
print('No. NOME                MÉDIA')
for p,n in enumerate(boletim):
    print(f'{p:<3} {n[0]:20}{((n[1][0]+n[1][1])/2):.2f}')
print('-'*30)
while True:
    op2 = int(input('Mostrar nota de qual aluno(a)?(999 para finalizar): '))
    if op2 == 999:
        print('Finalizado!')
        break
    if op2 <=len(boletim)-1:
        print(f'As notas do(a) aluno(a) {boletim[op2][0]} são {boletim[op2][1]}')
        print('-' * 50)
