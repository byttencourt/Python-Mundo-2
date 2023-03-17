par = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par += n
        cont += 1
print('Voce informou {}, número(s) pares e a soma foi {}.'.format(cont, par))
