while True:
    n = int(input('Gostaria de visualizar a tabuada de qual número? (numero negativo para parar): '))
    print('_'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('_'*20)
print('Fim!')
