import moeda, dado
c = ('\033[m',           # 0 = sem cor
    '\033[0;31m',        # 1 = vermelho
    '\033[0;32m',        # 2 = verde
    '\033[0;33m',        # 3 = amarelo
    '\033[0;34m',        # 4 = azul
    '\033[0;35m',        # 5 = roxo
    '\033[7;30m'         # 6 = preto
     )

while True:
    try:
        dado.titmenu('MENU PRINCIPAL', cor=0)
        dado.opmenu(1,'Ver pessoas cadastradas')
        dado.opmenu(2,'Cadastrar nova Pessoa')
        dado.opmenu(3,'Sair do Sistema')
        print('-'*50)
        op = (int(input('\033[32mSua Opção: ')))
        if op == 1:
            dado.titmenu('Opção 1')
        elif op == 2:
            dado.titmenu('Opção 2')
        elif op == 3:
            dado.titmenu('Saindo do sistema... Até Logo!',0)
            break
        elif op >= 4:
            print(f'{c[1]}ERRO!Digite uma opção válida!')
    except (TypeError, ValueError):
        print(f'{c[1]}ERRO! Digite uma valor númerico entre as opções!')
        continue