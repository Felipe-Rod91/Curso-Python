from random import randint
from time import sleep
numeros = []
cont = 0
print('-=' * 20)
print('JOGANDO NA MEGA-SENA')
print('-=' * 20)
jogos = int(input('Quantos jogos você deseja fazer? '))
print(f'Gerando {jogos} jogos...')
sleep(2)
while cont < jogos:
    while len(numeros) < 6:
        numero = randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
    sleep(0.3)
    cont += 1
    numeros.sort()
    print(f'Jogo {cont}: {numeros}')
    numeros.clear()
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
