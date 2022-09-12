n = cont = soma = 0
print('\033[31mOBS\033[m: o numero 999 é a condição de parada')
n = int(input('Informe um numero: '))
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Informe um numero: '))
print('Foram digitados {} numeros e a soma entre eles é {}'.format(cont, soma))