def ajuda(x):
    help(x)


comando = ''
while True:
    comando = str(input('Informe a função para saber sua biblioteca:  '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)