eu = {'nome': 'Gabriel', 'sexo': 'M', 'Idade': 18}
print(eu.values())
print(eu.keys())
print(eu.items())
for x,y in eu.items():
    print(f'{x} = {y}')

dados = {}
lista = []
for c in range(1,2):
    dados['Nome'] = str(input('Informe seu nome: '))
    dados['Idade'] = int(input('Informe sua idade: '))
    lista.append(dados.copy())
for c in lista:
    for x, y in c.items():
        print(f'{x} pertence a {y}')