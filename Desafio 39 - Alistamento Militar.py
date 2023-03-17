from datetime import date
import time
ano = int(input('qual seu ano de nascimento? '))
hoje = date.today().year
idade = hoje - ano
print('Sua idade é {}'.format(idade))
if idade < 18:
    print('Voce irá se alistar com 18 anos. Isso daqui ha {} ano(s).'.format(18-idade))
elif idade > 18:
    print('Você já deveria ter se alistado, faz {} anos'.format(idade - 18))
elif idade == 18:
    print('Compareça na junta militar mais proxima.')

