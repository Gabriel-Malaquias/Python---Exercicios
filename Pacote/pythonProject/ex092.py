from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando os valores...',end=' ')
    for c in range(0,5):
        x = randint(1,10)
        lista.append(x)
        print(x,end=' ')
        sleep(0.6)
    print()


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Dos valores da lista, a soma dos pares é {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)








