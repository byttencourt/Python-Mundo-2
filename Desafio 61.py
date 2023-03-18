p = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razao: '))
decimo = p + (10-1) * razao
while p < decimo+razao:
    print('{} ➜'.format(p * razao, end=' '))
print('Acabou!')