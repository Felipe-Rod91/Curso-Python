from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
sleep(1)
print('Você escolheu {}!'.format(itens[jogador]))
print('O computador escolheu {}!'.format(itens[computador]))
if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('VOCÊ VENCEU!')
elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
    print('VOCÊ PERDEU!')
elif jogador == computador:
    print('EMPATE!')
#Crie um programa que faça o computador jogar Jokenpô com você
