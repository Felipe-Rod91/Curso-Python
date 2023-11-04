from random import randint
from time import sleep
computador = randint(1, 5)
print('Estou pensando num número entre 1 e 5...')
sleep(2)
num = int(input('Em qual número estou pensando? '))
print('PROCESSANDO...')
sleep(3)
if num == computador:
    print('Parabéns! Era exatamente esse número =D')
else:
    print('ERROOOOUUU! Eu tava pensando no {}.'.format(computador))
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 1 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
