pa = int(input('Digite o valor max da pa: '))
razao = int(input('Digite a razão de sua PA: '))
for n in range(1, 11):
    for c in range(1, pa):
       if c % razao == 0:
            print(c)

