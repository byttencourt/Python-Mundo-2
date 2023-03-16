a = float(input('digite l1: '))
b = float(input('digite l1: '))
c = float(input('digite l3: '))
if a + b > c and a + c > b and b + c > a:
    print('É um triangulo')
elif a == b  and c == a:
    print('Equilatero')
elif (a == b and a != c) or (a != b and b == c):
    print('isosceles')
elif a != b and a != c and b != c:
    print('escaleno')
else:
    print('não é um triangulo')














else:
    print('Não é triangulo')