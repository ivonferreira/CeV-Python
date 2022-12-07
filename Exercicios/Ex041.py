from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <=9:
    cat = '\033[31mMIRIM\033[m'
elif idade <=14:
    cat = '\033[32mINFANTIL\033[m'
elif idade <=19:
    cat = '\033[33mJUNIOR\033[m'
elif idade <=20:
    cat = '\033[34mSENIOR\033[m'
else:
    cat = '\033[35mMASTER\033[m'
print('Sua idade é {} anos, logo sua categoria é {}'.format(idade, cat))

