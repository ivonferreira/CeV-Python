def notas(* valores, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    '''s = tot = maior = menor = media = 0
        for i,v in enumerate(valores):
        s +=v
        tot +=1
        if i == 1:
            maior = v
            menor = v
        if maior < v:
            maior = v
        if menor > v:
            menor =v
    media = s/ len(valores)
    boletim['total'] = tot
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['média'] = media'''
    boletim = dict()
    boletim['total'] = len(valores)
    boletim['maior'] = max(valores)
    boletim['menor'] = min(valores)
    boletim['média'] = sum(valores)/len(valores)
    if sit:
        if boletim['média'] >= 7.0:
            boletim['situação'] = 'BOA'
        elif boletim['média'] < 5.0:
            boletim['situação'] = 'RUIM'
        else:
            boletim['situação'] = 'RAZOÁVEL'
    return boletim


#programa principal
resp = notas(7.0, 8.2, 9.5, 1.2,2.0,3.1,1.1,1.0,10,0.5, sit=True)
print(resp)
help(notas)