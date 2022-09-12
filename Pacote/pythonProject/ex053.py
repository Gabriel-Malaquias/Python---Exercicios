while True:
    print('-'*50)
    v = int(input('\033[34mDiga o número no qual você deseja saber a tabuada\033[m: '))
    print('-'*50)
    for c in range(0,11):
        print(f'{v} x {c} = {v*c}')
    if c < 0:
        break
print('FIM')