ultimo = 1
penultimo = 1
n = int(input('Digite um número para visualizar a sequencia de fibonatti: '))
if n == 1 or n == 2:
    print('1')
else:
    c = 3
    while c <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        c += 1
        print('{},'.format(termo), end='')
print('fim')
