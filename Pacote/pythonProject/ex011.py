print('----------------- \n VAGAS DE EMPREGO \n --------------------')
nome = str(input('Digite seu nome: '))
print('Seja Bem Vindo {}'.format(nome))
idade = int(input('Para continuarmos, digite sua idade: '))
if idade >= 18:
    print('Meus parabéns, voce possui os requisitos minimos para concorrer a vaga !!!')
else:
    print('Lamentamos muito, voce nao possui idade suficiente para concorrer a vaga')

