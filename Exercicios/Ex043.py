peso = float(input('Qual seu peso? Sem mentir por favor: '))
alt = float(input('Qual sua altura? Agora você não diminuie né²: '))
imc = peso/(alt**2)
if imc < 18.5:
    sit = '\033[33mPeso baixo\033[m'
elif imc <25:
    sit = '\033[34mPeso ideal\033[m'
elif imc <30:
    sit = '\033[32mSobrepeso\033[m'
elif imc <40:
    sit = '\033[35mObesidade\033[m'
else:
    sit = '\033[31mObesidade Mórbida\033[m'
print('Seu IMC é {:.1f} e você está com {}' .format(imc, sit))