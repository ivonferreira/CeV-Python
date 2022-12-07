#from datetime import date
from datetime import datetime
dici = dict()
dici['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
#dici['idade'] = date.today().year - nasc
dici['idade'] = datetime.now().year - nasc
dici['ctps'] = int(input('CTPS:[0 para não tem] '))
if dici['ctps'] != 0:
    dici['contratacao'] = int(input('Ano de Contratação: '))
    dici['salario'] = float(input('Salário: '))
#    dici['aposentadoria'] = ((dici['contratacao']+35)- date.today().year) + dici['idade']
    dici['aposentadoria'] = ((dici['contratacao'] + 35) - datetime.now().year) + dici['idade']
for k,v in dici.items():
    print(f'{k} tem o valor {v}')