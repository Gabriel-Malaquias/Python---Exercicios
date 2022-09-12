nome = []
nome.append('Gabriel')
nome.append(18)
teste = []
teste.append(nome[:])
nome[0] = 'Gabriela'
nome[1] = 20
teste.append(nome[:])
print(teste)

turma = [['Joao', 18], ['Cleiton', 20], ['Maria', 25]]
for t in turma:
   print(f'{t[0]} tem {t[1]} anos de idade')

lista = []
dados = []
for c in range (0,4):
    dados.append(str(input('Informe seu nome: ')))
    dados.append(int(input('Informe sua idade: ')))
    lista.append(dados[:])
    dados.clear()
print(lista)