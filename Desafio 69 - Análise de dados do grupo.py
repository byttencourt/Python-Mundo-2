m18 = masc = mm20 = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        m18 += 1
    if sexo == 'M':
        masc += 1
    if idade < 20 and sexo == 'F':
        mm20 += 1
    print('-' * 30)
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if perg in 'N':
        break
print('-'*30)
print(f'Existe {m18} pessoas com mais de 18 anos.')
print(f'Existem ao todo {masc} homens cadastrados.')
print(f'Mulheres com menos de 20 anos = {mm20}.')
