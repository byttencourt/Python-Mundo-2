import datetime
print('-=-'*11)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-'*11)
ano = int(input('Ano de nascimento: '))
hoje = datetime.datetime.now()
year = hoje.year
idade = year - ano


if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade > 9 and (idade <= 14):
    print('CATEGORIA: INFANTIL')
elif idade > 14 and (idade <= 19):
    print('CATEGORIA: JUNIOR')
elif idade >= 19 and (idade <= 20):
    print('CATEGORIA: SENIOR')
elif idade > 20:
    print('CATEGORIA: MASTER')
print('---' * 11)
