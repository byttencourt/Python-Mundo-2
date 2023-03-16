valor = int(input('Valor do Produto: '))
print('-=-'*10)
print('Escolha a opção de Pagamento')
op = int(input('[1] À vista dinheiro ou  cheque.\n[2] À vista no Cartão.\n[3] Em até 2x no Cartão.\n[4] 3x ou mais\nOpção: '))
if op == 1:
    print('Opção com 10% de desconto')
    print('Valor a ser pago R${:.2f}'.format(valor - valor * 10/100))
elif op == 2:
    print('Opçao com 5% de desconto')
    print('Valor a ser pago R${:.2f}'.format(valor - valor * 5/100))
elif op == 3:
    print('Opção com parcelamento em até 2x de R${:.2f}.\nValor a ser pago R${:.2f}.'.format(valor/2, valor))
elif op == 4:
    print('Opção de parcelamento em 3x de R${:.2f}.\nValor a ser pago R${:.2f}'.format((valor + valor * 20 / 100)/3, valor + valor * 20 / 100))
else:
    print('Opção errada verifique sua opção.')
