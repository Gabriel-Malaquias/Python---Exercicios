print('-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=\n \033[33mANALISANDO UM TRIANGULO PART 2\033[m \n -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
reta1 = int(input('Valor da primeira reta: '))
reta2 = int(input('Valor da segunda reta: '))
reta3 = int(input('Valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('Os segmentos digitados podem formar um TRIÂNGULO', end = ' ')
    if reta1 == reta2 == reta3:
        print('\033[1;35mEQUILÁTERO\033[m')
    elif reta1 != reta2 != reta3 != reta1:
        print('\033[1;35mESCALENO\033[m')
    else:
        print('\033[1;35mISÓSCELES\033[m')
else:
    print('Os segmentos acima não podem formar um triângulo')