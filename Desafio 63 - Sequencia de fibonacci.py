penultimo = 1
ultimo = 2
n = int(input('Quantos termos da sequencia de fibonatti quer visualizar? '))
print('{},{},'.format(penultimo, ultimo), end='')
c = 3
while c <= n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    c += 1
    print('{},'.format(termo), end='')
print('fim')
