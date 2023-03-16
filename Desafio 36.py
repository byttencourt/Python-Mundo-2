valor = int(input('Valor da casa: '))
sal = int(input('Qual salário? '))
anos = int(input('Quantos anos vai pagar '))

pre = valor / (anos * 12)
print('O valor da prestação é R${:.2f}, para uma casa de R${:.2f}, em {} parcelas.'.format(pre, valor, anos * 12))

if pre > sal * 30 / 100:
    print('Seu imprestimo foi negado')
else:
    print('imprestimo concedido')

