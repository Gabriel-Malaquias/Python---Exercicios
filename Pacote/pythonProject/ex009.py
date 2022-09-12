inf = str(input('Diga sobre o que voce tem mais medo:')).strip().upper()
print('a letra A aparece {} vezes'.format(inf.count('A')))
print('a letra A aparece pela primeira vez na poscição {}'.format(inf.find('A')))
print('a letra A aparece pela ultima vez na posição {}'.format(inf.rfind('A')))

