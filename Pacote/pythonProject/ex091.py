from time import sleep


def maior(*num):
    cont = maior = 0
    print('~'*25)
    print(f'Processando os valores...')
    for c in num:
        print(f'{c}',end=' ')
        sleep(0.4)
        if cont == 0:
            maior = c
        else:
            c > maior
            maior = c
        cont += 1
    print(f'\nAo todo foram informados {cont} valores')
    print(f'O maior entre eles é {maior}')


maior(10, 15, 20, 45)


