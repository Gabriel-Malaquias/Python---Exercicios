print('---------------- \n RADAR \n ---------------')
veloc = float(input('O veículo estava a quantos Km/h ? '))
if veloc > 80:
    print('Excesso de velocidade !')
    multa = (veloc-80) * 7
    print('Sujeito a pagar multa de R${}'.format(multa))
else:
    print('Dentro do limite, tenha um bom dia e se beber nao dirija')

