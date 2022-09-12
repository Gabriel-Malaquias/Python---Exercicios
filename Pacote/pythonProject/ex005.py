nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo em maiúsculo é {}{}{}'.format(nome.upper()))
print('Seu nome completo em minúsculo é {}{}{}'.format(nome.lower()))
print('Ao todo, seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
sep = nome.split()
print('Seu primeiro nome é {}{}{} e tem {}{}{} letras'.format(sep[0], len(sep[0])))
print('Seu segundo nome é {} e tem {} letras'.format(sep[1], len(sep[1])))
print('Seu terceiro nome é {} e tem {} letras'.format(sep[2], len(sep[2])))

