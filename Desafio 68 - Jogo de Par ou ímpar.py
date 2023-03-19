from random import randint
c = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ->')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador escolheu {computador}. Total de {total}. ',end='')
    print('Deu Par!' if total % 2 == 0 else 'Deu Ímpar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    print('--' * 30)
    print('Vamos tentar novamente!')
print('--' * 30)
print(f'Game Over! Voce venceu {c} vezes.')




