menor = 0
maior = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(c)))
    if menor == 0:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor  = peso
print('Menor peso {}kg.\nMaior peso {}kg'.format(menor, maior))
