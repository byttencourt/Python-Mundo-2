total = m1000 = mbarato = 0
while True:
    print('='*30)
    print('{:-^30}'.format('Loja do Nicolas'))
    print('='*30)
    produto = str(input('Digite o nome do produto: ')).strip().title()
    preço = float(input('Qual valor do produto? '))
    total += preço
    if preço > 1000:
        m1000 += 1
    if mbarato == 0:
        mbarato = preço
        nomembarato = produto
    elif mbarato > preço:
        mbarato = preço
        nomembarato = produto
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if perg == 'N':
        break
print('{:=^30}'.format('FIM!'))
print(f'Total gasto na compra {total:.2f}')
print(f'{m1000} produtos custam mais de 1000.')
print(f'O produto mais barato é o {nomembarato} e custa {mbarato:.2f}')

