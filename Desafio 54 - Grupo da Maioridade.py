from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('menores = {}\nmaiores = {}'.format(menor, maior))
