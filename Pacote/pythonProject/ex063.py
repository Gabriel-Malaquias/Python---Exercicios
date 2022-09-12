lista = ('Saco de Ração', 165,
         'Peixe', 10,
         'Calopsita', 180,
         'Remédio', 50,
         'Gaiola', 150,
         'Petisco de cão', 5)
for produto in range (0, len(lista)):
    if produto % 2 == 0:
        print(f'{lista[produto]:.<25}',end=' ')
    else:
        print(f'R${lista[produto]:>5.2f}')