print('='*15)
print('GERADOR DE P.A')
print('='*15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
continuar = 10
while continuar != 0:
    total = total + continuar
    while c <= 10:
        print('{} => '.format(termo),end='')
        termo += razao
        c += 1
    print('PAUSA')
    continuar = int(input('Quantos deseja acrescentar ? '))
print('P.A finalizada com {} no total'.format(total))