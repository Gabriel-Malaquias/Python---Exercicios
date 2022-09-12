tot18 = totH = totM20 = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu gênero [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if idade <= 20 and sexo == 'F':
        totM20 +=1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar ? ')).strip().upper()[0]
    if cont == 'N':
            break

print('O total de pessoas com idade maior ou igual 18 anos foi {}'.format(tot18))
print('O total de homens cadastrados foi {}'.format(totH))
print('Por último, o total de mulheres com menos 20 anos cadastradas foi {}'.format(totM20))