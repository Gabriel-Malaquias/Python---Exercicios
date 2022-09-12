num = int(input('Informe um numero: '))
num2 = int(input('Informe mais outro numero: '))
if num > num2:
    print('O numero {} é \033[34mMAIOR\033[m do que o {}'.format(num, num2))
elif num < num2:
    print('O numero {} é \033[32mMENOR\033[m do que {}'.format(num, num2))
else:
    num == num2
    print('Os dois valores são \033[36mIGUAIS\033[m')