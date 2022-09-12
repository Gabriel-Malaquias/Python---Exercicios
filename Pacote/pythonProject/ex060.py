times = ('Palmeiras','Corinthians','Fluminense','Atletico-PR','Flamengo','Internacional','Atletico-MG',
         'Bragantino','Santos','América-MG','São Paulo','Botafogo','Goiás','Ceara','Coritiba','Avaí',
         'Fortaleza','Cuibá','Atletico-GO','Juventude')
for c in times:
    print(c)
print('='*25)
print('De acordo com a tabela...')
print('='*25)
print(f'Os primeiros times são {times[0:5]}')
print(f'Os quatro ultimos colocados foram {times[-4:]}')
print(f'Na ordem alfabética {sorted(times)}')
print(f'O flamengo esta na {times.index("Flamengo")+1} posição')