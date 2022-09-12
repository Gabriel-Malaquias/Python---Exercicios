def leiaInt(text):
    valid = False
    valor = 0
    while True:
        num = str(input(text))
        if num.isnumeric():
            valor = int(num)
            valid = True
        else:
            print('\033[31mERRO, digite apenas numeros. Tente novamente\033[m')
        if valid:
            break
    return valor


num = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {num}')