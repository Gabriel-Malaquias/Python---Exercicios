dados = {}
idade = list()
cont = contidade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    idade.append(int(input('Idade: ')))
    contidade += 1
    sum(idade)
    while True:
        dados['sexo'] = str(input('Sexo: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('ERRO. Informe Masculino ou Feminino')
    cont += 1
    while True:
        resp = str(input('Deseja continuar ? ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO. Digite sim ou não')
    if resp == 'N':
        break
print(f'Foram cadastradas {cont} pessoas')
media = sum(idade) / contidade
print((f'A média de idade é {media}'))
for c in dados:
    if dados['sexo'] == 'Ff':
        print(f'Na lista tem {c["nome"]} como mulher')

