peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura em metros ex: 1.82: '))
imc = peso / (altura ** 2)
print('Seu IMC {:.2f}.'.format(imc))
print('-=-'*10)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
