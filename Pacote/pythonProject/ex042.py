somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for c in range(1,5):
    print('======== {} pessoa ========'.format(c))
    nome = str(input('Nome da {} pessoa: '.format(c)))
    idade = int(input('Idade da {} pessoa: '.format(c)))
    sexo = str(input('Sexo M/F: '.format(c))).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade desse grupo é {}'.format(mediaidade))
print('A idade do homem mais velho é {} anos e ele se chama {}'.format(maioridadehomem, nomevelho ))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))