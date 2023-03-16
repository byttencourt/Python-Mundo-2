print('Conversor de Valores')
num = int(input('Digite o valor: '))
op = int(input('Escolha a base de conversão:\n[1] Para binário.\n[2] Para Octal.\n[3] Para Hexadecial.\n Sua Opção: '))
if op == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)))
elif op == 2:
    print('{} convertido para octal é {}.'.format(num, oct(num)))
elif op == 3:
    print('{} convertido para hexadecimal é {}.'.format(num, hex(num)))
else:
    print('Escolha entre 1 e 3.')

