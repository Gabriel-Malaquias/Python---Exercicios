from time import sleep


def contador(i, f, p):
    print('~'*40)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        for c in range(i, f, p):
            print(c,end=' ')
            sleep(0.5)
        print('FIM')
    elif i > f:
        for c in range(i, f, p):
            print(c,end=' ')
            sleep(0.5)
        print('FIM')


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, -2)
print('~'*40)
print('Agora é sua vez de fazer a contagem !')
inicio = int(input('Inicío:  '))
fim = int(input('Fim:  '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
