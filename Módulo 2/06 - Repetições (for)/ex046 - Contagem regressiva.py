# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

print('Iniciando a contagem:')
sleep(1)
for c in range(11, 0, -1):
    print(c-1)
    sleep(1)
print('FELIZ ANO NOVO!!!')
