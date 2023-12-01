# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
aleat = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os 5 números aleatórios são:', end=' ')
for num in aleat:
    print(f'{num} ', end='')
print(f'\nO maior número é {max(aleat)} e o menor é {min(aleat)}.')
