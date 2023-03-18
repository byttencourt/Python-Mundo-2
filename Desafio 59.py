from time import sleep
r = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
while r != 5:
    r = int(input('''
    ----- Qual Operação deseja realizar? -----
    [1] Somar
    [2] Multiplicar
    [3] maior
    [4] novos números
    [5] sair
    ------------------------------------------
    '''))
    if r == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}.'.format(n1, n2, soma))
    elif r == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multiplicação))
    elif r == 3:
        if n1 > n2:
            print('n1 = {} é maior que n2 = {}.'.format(n1, n2))
        else:
            print('n2 = {} é maior que n1 = {}.'.format(n2, n1))
    elif r == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o Segundo número: '))
    elif r == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('error')
print('Fim!')
