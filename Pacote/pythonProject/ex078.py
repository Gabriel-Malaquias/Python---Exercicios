lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota2:  '))
    media = nota1 + nota2 / 2
    lista.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*20)
print(f'{"Aluno":<5}  {"Nome":<5}    {"Media":>5}')
for x,y in enumerate(lista):
    print(f'{x:<5}  {y[0]}  {y[2]:>7.2f}')
print('-'*20)
while True:
    print('='*30)
    test = int(input('De qual aluno deseja saber as notas ? [OBS: 999 interrompe]: '))
    if test == 999:
        break
    if test <= len(lista):
        print(f'A nota do aluno {lista[test][0]} foi {lista[test][1]}')
