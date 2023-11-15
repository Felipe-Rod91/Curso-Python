#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep

print('=|=' * 5, 'ANALISADOR DE TRIÂNGULOS', '=|=' * 5)

l1 = float(input('Digite o comprimento da linha 1: '))
l2 = float(input('Digite o comprimento da linha 2: '))
l3 = float(input('Digite o comprimento da linha 3: '))
print('PROCESSANDO...')

sleep(2)
verde = '\033[1;32m'
vermelho = '\33[1;31m'
fecha = '\033[m'

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'As três linhas {verde} PODEM {fecha} formar um triângulo.')
else:
    print(f'As três linhas {vermelho} NÃO PODEM {fecha} formar um triângulo.'.format(vermelho, fecha))
