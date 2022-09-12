def notas(*test):
    """
    Função para analisar notas de alunos
    :param test:  recebe várias notas
    :return: retorna os valores adicionados no dicionário
    """
    x = dict()
    x['quant.notas'] = len(test)
    x['maior'] = max(test)
    x['menor'] = min(test)
    x['media'] = sum(test) / len(test)
    if x['media'] > 7:
        print('Situação: BOA')
    elif 5 < x['media'] < 7:
        print('Situação: RAZOÁVEL')
    else:
        x['media'] < 5
        print('Situação: PÉSSIMA')
    return x


resp = notas(4.5, 8.2, 6.3, 7.7, 10)
print(resp)
help(notas)