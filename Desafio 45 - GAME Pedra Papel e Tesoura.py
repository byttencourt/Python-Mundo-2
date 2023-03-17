from random import choice
print('✊PEDRA✊, ✋PAPEL✋ E ✌️TESOURA✌️')
escolha = str(input(' Qual sua escolha: ')).upper().strip()
print('Voce escolheu {}'.format(escolha))
lista = ['pedra', 'papel', 'tesoura']
sorteio = choice(lista).upper()
print('Computador escolheu: {}'.format(sorteio))
if escolha == 'PEDRA' and sorteio == 'TESOURA':
    print('VOCÊ GANHOU!')
elif escolha == 'TESOURA' and sorteio == 'PEDRA':
    print('VOCÊ PERDEU!')
elif escolha == 'TESOURA' and sorteio == 'PAPEL':
    print('VOCÊ GANHOU!')
elif escolha == 'PAPEL' and sorteio == 'TESOURA':
    print('VOCE PERDEU!')
elif escolha == 'PAPEL' and sorteio == 'PEDRA':
    print('VOCE GANHOU!')
elif escolha == 'PEDRA' and sorteio == 'PAPEL':
    print('VOCÊ PERDEU!')
else:
    print('EMPATE')

