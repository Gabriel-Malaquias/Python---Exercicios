print('=========\n \033[4;33mIMC\033[m \n=========')
peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura: '))
IMC = peso / (altura**2)
if IMC < 18.5:
    print('\033[1;31mABAIXO DO PESO\033[m')
elif IMC > 18.5 and IMC < 25:
    print('\033[1;31mPESO IDEAL\033[m')
elif IMC > 25 and IMC < 30:
    print('\033[1;31mSOBREPESO\033[m')
elif IMC > 30 and IMC < 40:
    print('\033[1;31mOBESIDADE\033[m')
else:
    IMC > 40
    print('\033[1;31mOBESIDADE MÓRBIDA\033[m')