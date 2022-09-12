print('============ \n ORÇAMENTO DE VIAGEM \n ================')
dist = float(input('Qual a distancia da viagem ? '))
print('Voce está prestes a fazer uma viagem de {}KM'.format(dist))
if dist <= 200:
    preço = dist * 0.50
    print('Para esta viagem, voce tera que pagar um total de R${}'.format(preço))
else:
    dist > 200
    preço1 = dist * 0.45
    print('Para esta viagem, voce tera que pagar um total de R${}'.format(preço1))

