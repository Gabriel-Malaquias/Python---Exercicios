import random
h1 = str(input('Diga o nome do primeiro aluno: '))
h2 = str(input('Diga o nome do segundo aluno: '))
h3 = str(input('Diga o nome do terceiro aluno: '))
lista = [h1, h2, h3]
sorteado = random.choice(lista)
print(' o nome sorteado foi {}{}{}'.format('\033[33m', sorteado, '\033[m'))