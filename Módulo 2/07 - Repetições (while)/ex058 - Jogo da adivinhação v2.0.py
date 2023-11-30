#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
#tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
tentativas = 0
print('Pensei em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... tente mais uma vez.')
        if jogador < computador:
            print('Mais... tente mais uma vez.')
print(f'PARABÉNS, VOCÊ ACERTOU! Eu estava pensando no {computador}.')
if tentativas == 1:
    print('VOCÊ ACERTOU DE PRIMEIRA, BRABO DEMAIS!')
else:
    print(f'Foram necessárias {tentativas} tentativas para acertar.')
