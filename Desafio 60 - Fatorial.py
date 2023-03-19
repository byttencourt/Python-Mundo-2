#from math import factorial
#n = int(input('Digite um número: '))
#f = factorial(n)
#print('O fatorial de {} é {}.'.format(n, f))

n = int(input('digite um fatorial: '))
c = n
f = 1
while c > 0:
    if c != 1:
        print('{} x '.format(c), end= '')
    else:
        print('{} ='.format(c), end= '')
    f *= c
    c -= 1
print('{}.'.format(f))

