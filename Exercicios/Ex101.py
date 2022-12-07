def voto(a):
    """
    Função para definir de acordo com ano de nascimento se está apto a votar no ano vigente
    :param a: Ano de nascimento
    :return: nao tem retorno
    """
    from datetime import date
    y = date.today().year
    idade = y - a
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos : NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


#programa principal
ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))