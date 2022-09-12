from random import randint
pc = (randint(0,10), randint(0,10), randint(0,10),
randint(0,10), randint(0,10))
print(pc)
print(f'Dos valores gerados, o maior é {max(pc)}')
print(f'E o menor, foi {min(pc)}')