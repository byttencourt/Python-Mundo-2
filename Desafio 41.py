from datetime import date
print('-=-'*11)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-'*11)
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Sua idade é {}.'.format(idade))
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade <= 25:
    print('CATEGORIA: SENIOR')
else:
    print('CATEGORIA: MASTER')
print('---' * 11)
