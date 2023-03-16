n1 = int(input('digite n1: '))
n2 = int(input('digite n2: '))
if n1 > n2:
    print('n1={} é maior que n2={}.'.format(n1, n2))
elif n2 > n1:
    print('n2={} é maior que n1={}'.format(n2, n1))
else:
    print('n1={} é igual a n2={}.'.format(n1, n2))