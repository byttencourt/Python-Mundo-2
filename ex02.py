r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        print('{} é um numero par.'.format(n))
    else:
        print('{} é um número ímpar.'.format(n))
    r = str(input('Deseja continuar? S/N: ')).upper().strip()
print('FIM!')
