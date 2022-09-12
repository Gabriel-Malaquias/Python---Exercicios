print('<<<<<<<<', '\033[35mAPROVEITAMENTO DE JOGADORES DE FUTEBOL\033[m', '>>>>>>>>')
jogo = {}
gols = list()
jogo['nome'] = str(input('Nome do canela: '))
part = int(input(f'Quantas partidas {jogo["nome"]} jogou ? '))
for c in range(0, part):
    gols.append(int(input(f'    Quantos gols na partida {c+1} ? ')))
jogo['gols'] = gols[:]
jogo['total'] = sum(gols)
print(jogo)
print('='*30)
for x,y in jogo.items():
    print(f'{x} pertence a {y}')
print('='*30)
for x, y in enumerate(gols):
    print(f'   Na partida {x+1}, fez {y} gols')
print(f'Total de {jogo["total"]} gols')
