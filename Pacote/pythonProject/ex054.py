print('='*30)
print('PARTIU JOGAR PAR OU IMPAR ? ')
print('='*30)
from random import randint
v = 0
while True:
    jog = int(input('Escolha um número: '))
    pc = randint (0, 10)
    total = jog + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: ')).strip().upper()[0]
    print(f'Você escolheu {jog} e o pc {pc}. Total de {total}')
    print('-'*30)
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[34mVocê Venceu\033[m')
            print('-'*30)
            v += 1
        else:
            print('\033[31mVocê Perdeu\033[m')
            print('-'*30)
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[34mVocê Venceu\033[m')
            print('-'*30)
            v += 1
        else:
            print('\033[31mVocê Perdeu\033[m')
            print('-'*30)
            break
print(f'Você ganhou {v} vezes')