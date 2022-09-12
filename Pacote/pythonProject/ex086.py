#TIPO 1
def lin():
    print('='*30)


lin()
print(' NOME ')
lin()
print(' GABRIEL MALAQUIAS ')
lin()
print(' GOSTO DE UMA XOXOTINHA')
lin()

#TIPO 2
def soma(a,b):
    s = a + b
    print(s)


soma(9,6)
soma(10,5)
soma(8,7)
soma(4,5)

#TIPO 3
def num(*dindin):
    tam = len(dindin)
    print(f'Recebi as notas de R${dindin} e ao todo foram {tam} cédulas')

num(50,20)
num(10,5,2)

#TIPO 4
def dobra(x):
    pos = 0
    while pos < len(x):
        x[pos] *= 2
        pos += 1


val = [4, 5, 2, 6, 7]
dobra(val)
print(val)