from datetime import date
ano = int(input('Que ano voce quer analisar ? Digite 0 para analisar o ano atual: '))
bis = ano % 4
if ano == 0:
    ano = date.today().year
if bis == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano NÃO É bissexto')