from random import randint
from time import sleep
lista = []
jogos = []
print('='*30)
print('         MEGA CENA    ')
print('='*30)
quant = int(input('Quantos jogos deseja que seja sorteado ? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        pc = randint(1,60)
        if pc not in lista:
            lista.append(pc)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for x,y in enumerate(jogos):
    print(f'Jogo{x+1}: {y}')
    sleep(1)
print('<'*10, 'BOA SORTE', '>'*10)