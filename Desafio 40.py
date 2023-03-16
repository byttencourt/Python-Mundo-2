n1 = float(input('nota1: '))
n2 = float(input('nota2: '))
media = (n1 + n2) / 2
print('A média é {}, primeira nota: {}, segunda nota: {}.'.format(media, n1, n2))
if media < 5:
    print('Reprovado')
elif 7 > media > 5:
    print('Recuperação')
elif media >= 7:
    print('Aprovado')
