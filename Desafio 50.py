par = 0
for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par = n + par
print(par)
