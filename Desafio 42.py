a = float(input('digite l1: '))
b = float(input('digite l1: '))
c = float(input('digite l3: '))
if a < b + c and b < a + c and c < a + b:
    print('É um triangulo ', end='')
    if a == b == c:
        print('Equilatero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('Não é triangulo')