print('Gerador de Progressão Aritmética')
p = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = p
c = 1
while c <= 10:
    print('{} ➡ '.format(termo), end='')
    termo += razao
    c += 1
print('fim')
