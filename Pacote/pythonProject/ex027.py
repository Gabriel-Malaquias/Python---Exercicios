from datetime import date
print('=================================\n \033[32mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m \n=================================')
nome = str(input('Informe o nome do atleta: '))
nasc = int(input('Informe o de nascimento deste atleta: '))
atual = date.today().year
idade = atual - nasc
if idade > 0 and idade < 9:
    print('O atleta tem {} anos'.format(idade))
    print('CLASSIFICAÇÃO: \033[33mMIRIM\033[m')
elif idade > 0 and idade < 14:
    print('O atleta tem {} anos'.format(idade))
    print('CLASSIFICAÇÃO: \033[33mINFANTIL\033[m')
elif idade > 0 and idade < 19:
    print('O atleta tem {} anos'.format(idade))
    print('CLASSIFICAÇÃO: \033[33mJÚNIOR\033[m')
elif idade > 0 and idade < 25:
    print('O atleta tem {} anos'.format(idade))
    print('CLASSIFICAÇÃO: \033[33mSÊNIOR\033[m')
else:
    idade > 25
    print('O atleta tem {} anos'.format(idade))
    print('CLASSIFICAÇÃO: \033[33mMASTER\033[m')
