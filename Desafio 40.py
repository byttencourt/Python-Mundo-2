n1 = float(input('nota1: '))
n2 = float(input('nota2: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado')
elif (media > 5) and (media < 7):
    print('Recuperação')
elif media == 7 or media > 7:
    print('Aprovado')
