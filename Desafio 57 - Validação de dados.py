r = 'a'
while r not in 'MFmf':
    r = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if r == 'M':
        print('Seu sexo é Masculino.')
    elif r == 'F':
        print('Seu sexo é Feminino')
    else:
        print('Escolha errada tente novamente!')
print('Fim!')
