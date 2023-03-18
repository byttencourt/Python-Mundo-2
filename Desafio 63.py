n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        c += 1
        soma += n
print('Foram digitados ao todo {} números. A soma deles totaliza {}.'.format(c, soma))
