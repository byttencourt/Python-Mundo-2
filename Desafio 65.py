c = 0
menor = 0
maior = 0
soma = 0
r = 's'
while r != 'N':
    n = int(input('Digite um número: '))
    if menor == 0:
        menor = n
    if menor > n:
        menor = n
    if maior < n:
        maior = n
    c += 1
    soma += n
    r = str(input('Deseja continuar? [S/N]: ')).upper()
print('A média entre os {} números digitados é {}'.format(c, soma/c))
print('o maior valor digitado é {} e o menor valor digitado é {}.'.format(maior, menor))


