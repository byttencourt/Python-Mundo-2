print('GERADOR DE PA BOMBADO!')
print('-='*12)
n = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = n
c = 1
p = 10
tot = 0
while p != 0:
    tot += p
    while c <= tot:
        print('{} ➡ '.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    p = int(input('Quantos termos quer mostrar a mais? '))
print('\nA progressao foi finalizada com {} termos mostrados.'.format(c))
