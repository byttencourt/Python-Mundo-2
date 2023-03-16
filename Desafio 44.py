valor = int(input('Valor do Produto: '))
print('-=-'*10)
print('Escolha a opção de Pagamento')
op = int(input('Opção 1: À vista dinheiro ou  cheque.\nOpção 2: À vista no Cartão.\nOpção 3: Em até 2x no Cartão.\nOpção 4: 3x ou mais\nOpção: '))
if op == 1:
    print('Opção com 10% de desconto')
    print('Valor a ser pago R${}'.format(valor - valor * 10/100))
elif op == 2:
    print('Opçao com 5% de desconto')
    print('Valor a se pago R${}'.format(valor - valor * 5/100))
elif op == 3:
    print('Opção com parcelamento em até 2x no cartão.\nValor a ser pago R${}.'.format(valor))
elif op == 4:
    print('Opção de parcelamento em 3x ou mais.\nValor a ser pago R${}'.format(valor + valor * 20 / 100))
