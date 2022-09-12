from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite mais um valor: '))
opção = 0
while opção != 5:
    print('-='*15)
    print('''SELECIONE A OPÇÃO DESEJADA
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS 
    [ 5 ] SAIR DO PROGRAMA''')
    print('-='*15)
    opção = int(input('Qual opção desejada ? '))
    if opção == 1:
        s = v1 + v2
        print('A \033[33mSOMA\033[m dos valores digitados é \033[31m{}\033[m'.format(s))
    elif opção == 2:
        m = v1 * v2
        print('A \033[33mMULTIPLICAÇÃO\033[m dos valores digitados é \033[31m{}\033[m'.format(m))
    elif opção == 3:
        if v1 > v2:
            maior = v1
            print('O \033[33mMAIOR\033[m valor foi \033[31m{}\033[m'.format(maior))
        else:
            v1 < v2
            maior = v2
            print('O \033[33mMAIOR\033[m valor foi \033[31{}\033[m'.format(maior))
    elif opção == 4:
        print('INFORME os valores novamente')
        v1 = int(input('\033[34mPrimeiro\033[m valor: '))
        v2 = int(input('\033[34mSegundo\033[m valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
print('Fim do programa')
