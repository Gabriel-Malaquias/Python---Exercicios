sex = str(input('Me fale se você tem uma piroca ou uma buceta: ')).strip().upper()
while sex not in 'PIROCA/BUCETA':
    print('\033[31mERRO\033[m')
    sex = str(input('Tente novemente. Informe seu sexo: ')).strip().upper()
print('Dados salvos com sucesso !!!')