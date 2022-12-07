print('\033[0;30;40mOlá, mundo!\033[m')
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'vermelhobranco':'\033[41m',
         'pretoebranco':'\033[7m'}
nome = input('Digite seu nome: ').strip()

if nome.upper() == 'IVON':
    print('O nome {}{}{} é um nome muito bonito!'.format(cores['vermelhobranco'], nome,cores['limpa']))
else:
    print('Seu nome é {}{}{}, tenha um {}BOM DIA{}'.format(cores['azul'],nome , cores['limpa'],cores['pretoebranco'], cores['limpa']))
