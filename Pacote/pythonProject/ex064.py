#LISTAGEM DE PALAVRAS COM VOGAIS
palavras = ('Trabalhar','Dinheiro','Familia','Pagar','Diversao','Putaria','Viver')
for x in palavras:
    print(f'\nNa palavra {x.upper()} temos as vogais ',end='')
    for l in x:
        if l in 'aeiou':
            print(l,end=' ')