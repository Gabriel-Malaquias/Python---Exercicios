resp = 'S'
cont = media = soma = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar ? '))
media = soma / cont
print('Dos valores digitados, o maior é {} e o menor é {}'.format(maior, menor))
print('A média entre eles é {}'.format(media))