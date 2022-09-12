from datetime import date
print('=============\nALISTAMENTO MILITAR\n=============')
nome = str(input('Informe seu nome: '))
nasc = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print('Você precisa procurar a junta militar mais proxima e se alistar')
elif idade < 18:
    print('Você tem {} anos'.format(idade))
    anos = 18 - idade
    print('Portanto, é necessário aguardar {} anos para se alistar'.format(anos))
else:
    idade > 18
    print('Você tem {} anos e já passou do seu perido de alistamento'.format(idade))
    alist = nasc + 18
    print('Você se alistou em {}'.format(alist))
