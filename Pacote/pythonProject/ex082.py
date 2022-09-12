from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho: '))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = int(input('Renda: R$'))
    dados ['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('='*30)
for x, y in dados.items():
    print(f'{x} igual a {y}')
