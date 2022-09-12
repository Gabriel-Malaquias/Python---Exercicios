cont = soma = 0
print('OBS: Use o numero \033[31m999\033[m para parar')
while True:
    n = int(input('Informe um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Ao todo, foram digitados {cont} numeros e a soma entre eles é {soma}')
