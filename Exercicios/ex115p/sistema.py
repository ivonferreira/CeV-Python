from lib.interface import *
from lib.Arquivo import *
from time import sleep

arq = 'bdados.txt'

#if arquivoExiste(arq):
#    print('Arquivo Encontrado')
#else:
#    print('Arquivo Não Encontrado')
#    criarArquivo(arq)
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa','Sair do Sistema'])
    if resposta == 1: #Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2: #Opção para cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...Até Logo!')
        break
    else:
        print('\033[31mERRO!Digite uma opção válida\033[m')
    sleep(2)