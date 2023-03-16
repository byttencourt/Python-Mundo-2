peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura em metros ex: 1.82: '))
imc = peso / (altura ** 2)
print('Seu IMC {:.2f}.'.format(imc))
print('-=-'*10)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and (imc < 25):
    print('Peso Ideal')
elif imc >= 25 and (imc < 30):
    print('Sobrepeso')
elif imc >= 30 and (imc < 40):
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')
