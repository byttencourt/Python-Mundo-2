c = 0
f = 1
n = int(input('Digite um número: '))
while n > c:
    print('{}x'.format(n), end='')
    n -= 1
    f = f * n
print('= {}'.(f))
