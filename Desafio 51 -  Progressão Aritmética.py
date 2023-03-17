p = int(input('Digite o valor Primeiro termo: '))
razao = int(input('Digite a razão de sua PA: '))
decimo = p + (10-1) * razao
for n in range(p, decimo+razao, razao):
    print('{} ➜'.format(n), end=' ')
print('ACABOU!')

