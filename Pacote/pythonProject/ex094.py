def voto(test):
    from datetime import date
    atual = date.today().year
    idade = atual - test
    if idade < 16:
        return f'Idade igual a {idade} anos. VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Idade igual a {idade} anos. VOTO OPCIONAL'
    else:
        return f'Idade igual {idade} anos. VOTO OBRIGATÓRIO'


nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))