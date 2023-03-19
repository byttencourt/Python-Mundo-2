c = 0
menor = 0
maior = 0
soma = 0
r = 's'
while r in 'Ss':
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
print(f'A média entre os {c} números digitados é {soma/c}')
print(f'o maior valor digitado é {maior} e o menor valor digitado é {menor}.')


