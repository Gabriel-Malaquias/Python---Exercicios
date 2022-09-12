print('========\nNOTAS\n=========')
nome = str(input('Nome do aluno: '))
n1 = float(input('Nota do aluno no primeiro bimestre: '))
n2 = float(input('Nota do aluno no segundo bimestre: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('REPROVADO')
elif m > 5.0 and m < 6.9:
    print('RECUPERAÇÃO')
else:
    m >= 7.0
    print('APROVADO')
