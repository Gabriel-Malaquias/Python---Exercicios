nome = str(input('Digite seu nome completo: ')).strip()
posição = nome.split()
print('Seu primeiro nome é {}'.format(posição[0]))
print('Seu ultimo é {}'.format(posição[len(posição)-1]))