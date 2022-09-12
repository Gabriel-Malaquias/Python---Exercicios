dados = {}
while True:
    dados['Nome'] = str(input('Nome do Aluno: '))
    dados['Nota1'] = float(input('Nota 1: '))
    dados['Nota2'] = float(input('Nota 2: '))
    dados['media'] = (dados['Nota1'] + dados['Nota2']) / 2
    resp = str(input('Deseja continuar ? '))
    if resp in 'Nn':
        break
    elif dados['media'] <= 6:
        dados['Situação'] = 'Reprovado'
    else:
        dados['Situação'] = 'Aprovado'
    print('='*30)
    for x, y in dados.items():
        print(f'{x} é igual a {y}')
    print('='*30)
