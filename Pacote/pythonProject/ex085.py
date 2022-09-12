print('<'*8, '\033[32mAPROVEITAMENTO DE JOGADORES\033[m', '>'*8)
time = list()
jogo = {}
gol = list()
while True:
    jogo.clear()
    jogo['nome'] = str(input('Nome do canela: '))
    part = int(input(f'Quantas partidas {jogo["nome"]} jogou ? '))
    gol.clear()
    for c in range (0, part):
        gol.append(int(input(f'   Quantos gols na partida {c+1} ? ')))
    jogo['gol'] = gol[:]
    jogo['total'] = sum(gol)
    time.append(jogo.copy())
    while True:
        resp = str(input('Deseja continuar ? ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda Sim ou Não')
    if resp == 'N':
        break
print('=-'*30)
print(' jogador ',end='')
for x in jogo.keys():
    print(f'{x:<15}',end='')
print()
print('=-'*30)
for x,y in enumerate(time):
    print(f'{x:>3} ',end='')
    for c in y.values():
        print(f'{str(c):<15}', end='')
    print()
print('=-' * 30)





